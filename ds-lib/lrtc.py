#!/usr/bin/env python

import gzip
import numpy as np

k_cache={}
def k_complexity(value, label, memoize=True):
		"""
		Estimate Kolmgorov complexity of a string using compression. Optionally, memoize these results.
		"""
		if memoize and label in k_cache:
				return k_cache[label]
		ret=len(gzip.compress(value.encode()))
		if memoize:
				k_cache[label]=ret
		return ret

def lrtc(test_set, training_set, k):
		"""
		Low Resource Text Classifier, based on Jiang, et al (2023)
		"""
		ret=[]
		for (x1, label1) in test_set:
				Cx1 = k_complexity(x1, label1)
				distance_from_x1 = []
				for (x2, label2) in training_set:
						Cx2 = k_complexity(x2, label2)
						x1x2 = " ".join([x1, x2])
						Cx1x2 = k_complexity(x1x2, " ".join([label1, label2]))
						ncd = Cx1x2 - min(Cx1, Cx2) / max(Cx1, Cx2)
						distance_from_x1.append(ncd)
				sorted_idx = np.argsort(np.array(distance_from_x1))
				top_k_class = training_set[sorted_idx[:k], 1]
				predict_class = max(set(top_k_class), key=top_k_class.count)
				ret.append(predict_class)
		return ret

