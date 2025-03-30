
# -*- coding: utf-8 -*-
"""
Created on Sun March  30 08:345:47 2025

@author: IAN CARTER KULANI

"""

import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, messagebox

class NetworkGraphBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Graph Builder")
        
        self.graph = nx.Graph()
        
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()
        
        self.add_node_button = tk.Button(root, text="Add Node", command=self.add_node)
        self.add_node_button.pack()
        
        self.add_edge_button = tk.Button(root, text="Add Edge", command=self.add_edge)
        self.add_edge_button.pack()
        
        self.draw_button = tk.Button(root, text="Draw Graph", command=self.draw_graph)
        self.draw_button.pack()
        
        self.export_button = tk.Button(root, text="Export Graph", command=self.export_graph)
        self.export_button.pack()
    
    def add_node(self):
        node = simpledialog.askstring("Input", "Enter node name:")
        if node:
            self.graph.add_node(node)
            messagebox.showinfo("Success", f"Node '{node}' added!")
    
    def add_edge(self):
        node1 = simpledialog.askstring("Input", "Enter first node name:")
        node2 = simpledialog.askstring("Input", "Enter second node name:")
        if node1 and node2:
            self.graph.add_edge(node1, node2)
            messagebox.showinfo("Success", f"Edge between '{node1}' and '{node2}' added!")
    
    def draw_graph(self):
        plt.figure(figsize=(6,4))
        nx.draw(self.graph, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
        plt.show()
    
    def export_graph(self):
        nx.write_gml(self.graph, "network_graph.gml")
        messagebox.showinfo("Success", "Graph exported as 'network_graph.gml'!")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkGraphBuilder(root)
    root.mainloop()