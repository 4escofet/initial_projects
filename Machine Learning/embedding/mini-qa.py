from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthenticator
from datasets import load_dataset
# We import usser information and keys from config for security issues
from config import astra_clientId, astra_keyspace_name, astra_DB_name, astra_secret, ASTRA_DB_TOKEN_JSON_PATH, ASTRA_DB_SECURE_BUNDLE_PATH, OAI_client_id, OAI_client_secret
from cassandra.auth import PlainTextAuthProvider
import json

# enter the path to your secure connect bundle 'secure-connect***.zip'
ASTRA_DB_SECURE_BUNDLE_PATH = ASTRA_DB_SECURE_BUNDLE_PATH
# enter the path to your token details json file '***-token.json'
ASTRA_DB_KEYSPACE = astra_keyspace_name
ASTRA_DB_TOKEN_JSON_PATH = ASTRA_DB_TOKEN_JSON_PATH
OPENAI_API_KEY = OAI_client_secret

# Setting connection session configuration 
cloud_config= {
  "secure_connect_bundle": ASTRA_DB_SECURE_BUNDLE_PATH
}
with open(ASTRA_DB_TOKEN_JSON_PATH) as f:
    secrets = json.load(f)
ASTRA_DB_APPLICATION_TOKEN = secrets["token"] # token is pulled from your token json file

auth_provider=PlainTextAuthProvider("token", ASTRA_DB_APPLICATION_TOKEN)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
astraSession = cluster.connect()
print("Astra DB connection ready")

llm = OpenAI(openai_api_key=OPENAI_API_KEY)
myEmbedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# Table creation in Cassandra

myCassandraVStore = Cassandra(
    embedding = myEmbedding,
    session = astraSession,
    keyspace = astra_keyspace_name,
    table_name = "qa_mini_demo",
)

# Retriving data from huggingface and selecting headlines
print("Loading data from huggingface")
myDataset = load_dataset("Biddls/Onion_News", split="train")
headlines = myDataset["text"][:50]

# Generating embeddings and storing them into Cassandra database
print("\Generating embedding and storing in AstraDB")
myCassandraVStore.add_texts(headlines)

print("Inserted %i headlines.\n" % len(headlines))

vectorIndex = VectorStoreIndexWrapper(vectorstore=myCassandraVStore)

first_question = True
while True:
    if first_question:
        query_text = input("\nEnter your question (or type 'quit' to exit): ")
        first_question = False
    else:
        query_text = input("\nWhat's your next question (or type 'quit' to exit): ")

    if query_text.lower() == "quit":
        break

    print("QUESTION: \"%s\"" % query_text)
    answer = vectorIndex.query(query_text, llm=llm).strip()
    print("ANSWER: \"%s\"\n" % answer)

    print("DOCUMENTS BY RELEVANCE:")
    for doc, score in myCassandraVStore.similarity_search_with_score(query_text, k=4):
        print("  %0.4f \"%s ...\"" % (score, doc.page_content[:60]))