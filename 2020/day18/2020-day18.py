from treelib import Node, Tree
input_filename = "test_input.txt"
#pp = pprint.PrettyPrinter(indent=2)

class Node:
    def __init__(self, value = None):
        self.left  = None
        self.right = None
        self.value = value

def	part1(equations):
	tree = Tree()

	for eq in equations:
		build_tree(eq)
		break

def build_tree(equation):
	equation = equation.replace('(', '( ')
	equation = equation.replace(')', ' )')
	items = equation.split(' ')
	tree = Tree()
	root = tree.create_node(tag='empty')
	print(root)
	tree.show()
	last_node = None
	last_tree = None

	current_node = root
	for op in items:
		print("Adding {0} to the tree".format(op))
		print("Current Node: {0}".format(current_node))

		if op is ' ':
			pass
		elif op in ['+','*']:
			# Climb until you find an empty node or a root node
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
			print("Creating a new tree")
			last_node, last_tree = current_node, tree
			# Create the new tree with
			new_tree = Tree()
			node = new_tree.create_node(tag='empty')
			tree = new_tree
			current_node = node
		elif op.strip() is ')':
			print("Close the current tree and paste it onto the last tree")
			last_tree.paste(last_node.identifier, tree)
			current_node = last_node
			tree = last_tree

		tree.show()

	print("\n --- Final Tree ---")
	# tree.show()

def part2(fields, valid_tickets):
	pass

def main():
	equations = load_input_file()

	print("\n--- Part 1 ---")
	part1(equations)

	#print("\n--- Part 2 ---")
	#result = part2(fields, valid_tickets)	

def load_input_file():
	equations = []
	
	with open(input_filename) as f:
		equations = f.read().splitlines()	
	
	return equations

if __name__=="__main__":
	main()