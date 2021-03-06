import sys
import SPT_dijk as spt
import random 
import reading_graph_txt as rd
import dij_tree_tabu as di
import timeit
sys.path.append("../")
from Util import util

def cost_tree_grasp(nodes, tree):
    cost = util.blabla(nodes, tree)
    return cost

def grasp(nodes, edges):
	start = timeit.default_timer()
	lll =spt.loop_root_SPT(nodes,edges)
	stop = timeit.default_timer()
	print("Time for Dijkstra tree generator: " + str(stop-start))
	trees = []
	grasp_list = []
	for ll in lll:
		temp_tree = []
		for lis in ll:
			for ed in lis:
				if(di.edge_in_list(ed,temp_tree)):
					pass
				else:
					temp_tree.append(ed)
		trees.append(temp_tree)

	trees.sort(key = lambda x: cost_tree_grasp(nodes, x))
	mincost = util.blabla(nodes,trees[0])

	res = trees[random.randint(0,2)]
	grasp_cost_res = util.blabla(nodes, res)


	return res, grasp_cost_res, mincost 