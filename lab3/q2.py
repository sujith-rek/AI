# 2. Bayesian Belief Networks: 10*4=40
# Problem Statement:
# You are given a dataset containing information about weather conditions (Temperature,
# Humidity, Wind, and Outlook) and whether people played tennis or not. Your task is to
# implement a Bayesian Belief Network (BBN) to predict whether people will play tennis based on
# the given weather conditions.
# Requirements:
# 1. Implement a Bayesian Belief Network (BBN) from scratch using a programming language of
# your choice (e.g., Python, Java, etc.).
# 2. The BBN should consist of nodes representing the following variables: Temperature,
# Humidity, Wind, Outlook, and PlayTennis.
# 3. Use the dataset provided to learn the conditional probability tables (CPTs) for each node.
# 4. Implement the inference algorithm (e.g., Variable Elimination) to make predictions about
# whether people will play tennis given specific weather conditions.
# Dataset:
# | Outlook | Temperature | Humidity | Wind | PlayTennis |
# |---------|-------------|----------|------|------------|
# | Sunny | Hot | High | Weak | Yes |
# | Sunny | Hot | High | Strong | No |
# | Sunny | Cool | Normal | Weak | Yes |
# | Sunny | Mild | High | Weak | No |
# | Sunny | Mild | Normal | Strong | Yes |
# | Rain | Mild | High | Strong | No |
# | Rain | Mild | High | Weak | Yes |
# | Rain | Cool | Normal | Weak | Yes |
# | Rain | Cool | Normal | Strong | No |
# | Rain | Mild | Normal | Weak | Yes |
# | Overcast | Cool | Normal | Strong | Yes |
# | Overcast | Hot | High | Weak | Yes |
# | Overcast | Mild | High | Strong | Yes |
# | Overcast | Hot | Normal | Weak | Yes |

class Node:
    
    def __init__(self, name, parents, cpt):
        self.name = name
        self.parents = parents
        self.cpt = cpt

    def __str__(self):
        return self.name

class CustomBayesModel:

    def __init__(self, nodes):
        self.nodes = nodes
    
    def get_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None
    
    def get_parents(self, node):
        parents = []
        for parent in node.parents:
            parents.append(self.get_node(parent))
        return parents
    
    def get_children(self, node):
        children = []
        for child in self.nodes:
            if node.name in child.parents:
                children.append(child)
        return children
    
    def add_edge(self, parent, child):
        child.parents.append(parent.name)
    
    def remove_edge(self, parent, child):
        child.parents.remove(parent.name)
    
    def get_ancestors(self, node):
        ancestors = []
        parents = self.get_parents(node)
        for parent in parents:
            ancestors.append(parent)
            ancestors.extend(self.get_ancestors(parent))
        return ancestors
    
    def get_descendants(self, node):
        descendants = []
        children = self.get_children(node)
        for child in children:
            descendants.append(child)
            descendants.extend(self.get_descendants(child))
        return descendants
    
    def get_independent_nodes(self, node):
        independent_nodes = []
        for node in self.nodes:
            if node not in self.get_ancestors(node) and node not in self.get_descendants(node):
                independent_nodes.append(node)
        return independent_nodes
    
    def get_conditional_probability(self, node, evidence):
        parents = self.get_parents(node)
        if len(parents) == 0:
            return node.cpt[0][1]
        else:
            for row in node.cpt:
                if row[0] == evidence:
                    return row[1]
        return None
    
    def get_probability(self, node, evidence):
        parents = self.get_parents(node)
        if len(parents) == 0:
            return node.cpt[0][1]
        else:
            for row in node.cpt:
                if row[0] == evidence:
                    return row[1]
        return None
    
    def get_probability_of_evidence(self, evidence):
        probability = 1
        for node in self.nodes:
            
            if node.name in evidence:
                probability *= self.get_conditional_probability(node, evidence[node.name])
            
        return probability
    
    def get_probability_of_evidence_given(self, evidence, node):
        probability = 1
        for node in self.nodes:
            if node.name in evidence:
                probability *= self.get_probability(node, evidence[node.name])
        return probability
    
    # Inference method which will conclude if PlayTennis is Yes or No based on the given evidence
    def inference(self, evidence):
        probability = self.get_probability_of_evidence(evidence)
        probability_yes = self.get_probability_of_evidence_given(evidence, self.get_node('PlayTennis'))

        print('Probability of evidence: ', probability)
        print('Probability of evidence given PlayTennis: ', probability_yes)

        return probability_yes / probability
    

newBayesModel = CustomBayesModel([
    Node('Outlook', [], [
        [['Sunny'], 5/14],
        [['Overcast'], 4/14],
        [['Rain'], 5/14]
    ]),
    Node('Temperature', [], [
        [['Hot'], 4/14],
        [['Mild'], 6/14],
        [['Cool'], 4/14]
    ]),
    Node('Humidity', [], [
        [['High'], 7/14],
        [['Normal'], 7/14]
    ]),
    Node('Wind', [], [
        [['Weak'], 8/14],
        [['Strong'], 6/14]
    ]),
    Node('PlayTennis', ['Outlook', 'Temperature', 'Humidity', 'Wind'], [
        [['Sunny', 'Hot', 'High', 'Weak'], 2/9],
        [['Sunny', 'Hot', 'High', 'Strong'], 0/9],
        [['Overcast', 'Hot', 'High', 'Weak'], 4/9],
        [['Rain', 'Mild', 'High', 'Weak'], 3/9],
        [['Rain', 'Cool', 'Normal', 'Weak'], 2/9],
        [['Rain', 'Cool', 'Normal', 'Strong'], 0/9],
        [['Overcast', 'Cool', 'Normal', 'Strong'], 4/9],
        [['Sunny', 'Mild', 'High', 'Weak'], 0/9],
        [['Sunny', 'Cool', 'Normal', 'Weak'], 3/9],
        [['Rain', 'Mild', 'Normal', 'Weak'], 2/9],
        [['Sunny', 'Mild', 'Normal', 'Strong'], 6/9],
        [['Overcast', 'Mild', 'High', 'Strong'], 4/9],
        [['Overcast', 'Hot', 'Normal', 'Weak'], 4/9],
        [['Rain', 'Mild', 'High', 'Strong'], 0/9]
    ])
])

print(newBayesModel.get_probability_of_evidence({
    'Outlook': 'Sunny',
    'Temperature': 'Cool',
    'Humidity': 'High',
    'Wind': 'Strong'
}))

print(newBayesModel.get_probability_of_evidence({
    'Outlook': 'Rain',
    'Temperature': 'Mild',
    'Humidity': 'High',
    'Wind': 'Weak'
}))

print(newBayesModel.get_probability_of_evidence({
    'Outlook': 'Overcast',
    'Temperature': 'Hot',
    'Humidity': 'Normal',
    'Wind': 'Weak'
}))

print(newBayesModel.inference({
    'Outlook': 'Sunny',
    'Temperature': 'Cool',
    'Humidity': 'Normal',
    'Wind': 'Strong'
}))



