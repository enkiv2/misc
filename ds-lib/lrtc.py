#!/usr/bin/env python

import gzip
import numpy as np

def lrtc(test_set, training_set, k):
		"""
		Low Resource Text Classifier, based on Jiang, et al (2023)
		"""
		ret=[]
		for (x1, _) in test_set:
				Cx1 = len(gzip.compress(x1.encode()))
				distance_from_x1 = []
				for (x2, _) in training_set:
						Cx2 = len(gzip.compress(x2.encode()))
						x1x2 = " ".join([x1, x2])
						Cx1x2 = len(gzip.compress(x1x2.encode()))
						ncd = Cx1x2 - min(Cx1, Cx2) / max(Cx1, Cx2)
						distance_from_x1.append(ncd)
				sorted_idx = np.argsort(np.array(distance_from_x1))
				top_k_class = training_set[sorted_idx[:k], 1]
				predict_class = max(set(top_k_class), key=top_k_class.count)
				ret.append(predict_class)
		return ret

