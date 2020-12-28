from treelib import Node, Tree
input_filename = "input.txt"

op_precedence = {
	'*': 0,
	'+': 1,
	'(': 2,
	')': 2
}

def	part1(equations):
	values = []
	for eq in equations:
		tree = build_tree_pt1(eq)
		result = solve_tree(tree, tree.get_node(tree.root))
		values.append(result)

	print("Result: {0}".format(sum(values)))

def compute(ops, numbers):
	s = ops.pop()
	a, b = numbers.pop(), numbers.pop()
	if s is '*':
		result =  a * b
	elif s is '+':
		result = a + b
	return result

def solve_tree(tree, node):
	if node.is_leaf():
		return node.tag
	else:
		children_ids = node.successors(tree.identifier)
		vals = []
		for child_id in children_ids:
			result = None
			child = tree.get_node(child_id)
			val = solve_tree(tree, child)
			vals.append(int(val))

		op = node.tag
		if op is '+':
			return vals[0] + vals[1]
		elif op is '*':
			return vals[0] * vals[1]

def build_tree_pt1(equation):
	# https://stackoverflow.com/questions/24520841/how-to-build-a-parse-tree-of-a-mathematical-expression
	tree = Tree()
	root = tree.create_node(tag='empty')
	nodes = [] # stack for nodes
	trees = [] # stack for trees
	current_node = root

	for op in equation:
		if op in ['', ' ']:
			pass
		elif op in ['+','*']:
			# If the current node is not empty or a root node, climb  until you find an empty node or a root node
			if current_node.is_root() or current_node.tag == 'empty':
				pass
			else:
				while True:
					parent_id = current_node.predecessor(tree_id=tree.identifier)
					parent = tree.get_node(parent_id)
					current_node = parent
					if current_node.is_root() or current_node.tag == 'empty':
						break
		
			if current_node.tag == 'empty':
				current_node.tag = op
			elif current_node.is_root():
				new_tree = Tree()
				node = new_tree.create_node(tag=op)
				new_tree.paste(node.identifier, tree)
				tree = new_tree
				current_node = node
		elif op.isnumeric():
			new = tree.create_node(tag=op, parent=current_node.identifier)
			current_node = new
		elif op.strip() is '(':
			nodes.append(current_node) # push current node onto stack to save it
			trees.append(tree) # push current tree onto stack to save it
			# Create the new tree
			new_tree = Tree()
			node = new_tree.create_node(tag='empty')
			tree = new_tree
			current_node = node
		elif op.strip() is ')':
			# Pop last tree and node off the stack to know where to paste the current tree
			last_tree = trees.pop()
			last_node = nodes.pop()
			last_tree.paste(last_node.identifier, tree)
			current_node = last_node
			tree = last_tree
	
	# print("\n --- Final Tree ---")
	# tree.show()
	return tree

def	part2(equations):
	# https://stackoverflow.com/questions/28256/equation-expression-parser-with-precedence
	values = []
	for eq in equations:
		numbers = [] # stack for numbers
		ops = [] # stack for operands
		for item in eq:
			if item.isnumeric():
				numbers.append(int(item))
			elif item in ['+', '*']:
				while len(ops) != 0 and ops[-1] in ['+', '*']:
					if op_precedence[item] > op_precedence[ops[-1]]:
						break
					else:
						numbers.append(compute(ops, numbers))
				ops.append(item)
			elif item is '(':
				ops.append(item)
			elif item is ')':
				while (len(ops) != 0) and ops[-1] != '(':
					numbers.append(compute(ops, numbers))
				ops.pop()

		# We've run out of input, empty the stacks to computer the result
		while (len(ops) > 0) and (len(numbers) > 1):
			numbers.append(compute(ops, numbers))

		result = numbers[0]
		values.append(result)

	print("Result: {0}".format(sum(values)))


def main():
	equations = load_input_file()

	#print("\n--- Part 1 ---")
	#part1(equations)

	print("\n--- Part 2 ---")
	result = part2(equations)	

def load_input_file():
	equations = []
	
	with open(input_filename) as f:
		equations = f.read().splitlines()	
	
	for i,eq in enumerate(equations):
		eq = eq.replace('(', '( ').replace(')', ' )')
		equations[i] = eq.split(' ')

	return equations

if __name__=="__main__":
	main()