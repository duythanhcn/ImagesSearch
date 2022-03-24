import numpy as np
import csv

class Searcher:
	def __init__(self, indexPath):
		self.indexPath = indexPath

	def searchIMG(self, queryFeatures, limit = 20):
		results = {}

		with open(self.indexPath) as f:
			reader = csv.reader(f)
			for row in reader:
				features = [float(x) for x in row[1:]]
				d = self.calcChiSquareDistance(features, queryFeatures)
				results[row[0]] = d

			f.close()

		results = sorted([(a, b) for (b, a) in results.items()])

		return results[:limit]

	def calcChiSquareDistance(self, histA, histB, eps = 1e-10):
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])

		return d