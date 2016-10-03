import json

with open('quora-sample.txt', 'r') as inFile:
	inputHits = json.load(inFile)

docs = []

for doc in inputHits['hits']['hits']:
	docs.append(json.dumps(doc['_source']['sTitle'] + ', ' + doc['_source']['sConcepts'][0]))

sortedDocs = sorted(docs)
dupeCandidates = []

i = 0

for result in sortedDocs:
	while i < len(sortedDocs) - 1:
		if result == sortedDocs[i + 1]:
			dupeCandidates.append(result)
			dupeCandidates.append(sortedDocs[i + 1])
		i += 1

for result in dupeCandidates:
	print result
