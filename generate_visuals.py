import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import os

# Ensure directory exists
os.makedirs('visualizations', exist_ok=True)

def set_style():
    plt.style.use('dark_background')
    plt.rcParams['figure.facecolor'] = '#0f172a'
    plt.rcParams['axes.facecolor'] = '#1e293b'
    plt.rcParams['text.color'] = '#f1f5f9'
    plt.rcParams['axes.labelcolor'] = '#94a3b8'
    plt.rcParams['xtick.color'] = '#94a3b8'
    plt.rcParams['ytick.color'] = '#94a3b8'
    plt.rcParams['axes.edgecolor'] = '#334155'
    plt.rcParams['grid.color'] = '#334155'

def visualize_lab3_data():
    print("Generating Lab 3 visualization...")
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "Salary": [50000, 60000, 70000]
    }
    df = pd.DataFrame(data)
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(df["Name"], df["Salary"], color=['#6366f1', '#8b5cf6', '#ec4899'])
    
    plt.title('Employee Salary Distribution (Lab 3)', fontsize=16, pad=20, color='#f1f5f9')
    plt.xlabel('Employee Name', fontsize=12)
    plt.ylabel('Salary ($)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:,}',
                ha='center', va='bottom', color='#f1f5f9')
                
    plt.savefig('visualizations/lab03_salary_analysis.png', bbox_inches='tight', dpi=300)
    plt.close()

def visualize_lab4_graph():
    print("Generating Lab 4 visualization...")
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F', 'G'},
        'D': {'B'},
        'E': {'B', 'H'},
        'F': {'C'},
        'G': {'C'},
        'H': {'E'}
    }
    
    G = nx.Graph(graph)
    pos = nx.spring_layout(G, seed=42)
    
    plt.figure(figsize=(10, 8))
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='#6366f1', node_size=1000, alpha=0.8)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color='#94a3b8', width=2, alpha=0.5)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_color='white', font_size=12, font_weight='bold')
    
    plt.title('Graph Structure for BFS/DFS (Lab 4)', fontsize=16, pad=20, color='#f1f5f9')
    plt.axis('off')
    
    plt.savefig('visualizations/lab04_graph_structure.png', bbox_inches='tight', dpi=300, facecolor='#0f172a')
    plt.close()

def visualize_lab5_astar():
    print("Generating Lab 5 A* visualization...")
    # Graph with weights
    edges = [
        ('A', 'B', 1), ('A', 'C', 4),
        ('B', 'D', 2), ('B', 'E', 5),
        ('C', 'F', 3), ('C', 'G', 2), # Note: G is connected to F in original code, fixing for visual
        ('D', 'B', 2),
        ('E', 'H', 2),
        ('F', 'G', 2),
        ('G', 'F', 2),
        ('H', 'E', 2)
    ]
    
    # Recreating the graph structure from Lab 5 code exactly
    # A->B(1), A->C(4)
    # B->A(1), B->D(2), B->E(5)
    # C->A(4), C->F(3)
    # D->B(2)
    # E->B(5), E->H(2)
    # F->C(3), F->G(2)
    # G->F(2)
    # H->E(2)
    
    G = nx.Graph()
    G.add_edge('A', 'B', weight=1)
    G.add_edge('A', 'C', weight=4)
    G.add_edge('B', 'D', weight=2)
    G.add_edge('B', 'E', weight=5)
    G.add_edge('C', 'F', weight=3)
    G.add_edge('F', 'G', weight=2)
    G.add_edge('E', 'H', weight=2)
    
    pos = nx.spring_layout(G, seed=42)
    
    plt.figure(figsize=(12, 8))
    
    # Path found: A -> C -> F -> G
    path_edges = [('A', 'C'), ('C', 'F'), ('F', 'G')]
    other_edges = [e for e in G.edges() if tuple(sorted(e)) not in [tuple(sorted(p)) for p in path_edges]]
    
    # Draw all nodes
    nx.draw_networkx_nodes(G, pos, node_color='#1e293b', edgecolors='#6366f1', node_size=1000, linewidths=2)
    
    # Draw path nodes highlighted
    path_nodes = ['A', 'C', 'F', 'G']
    nx.draw_networkx_nodes(G, pos, nodelist=path_nodes, node_color='#ec4899', node_size=1000)
    
    # Draw non-path edges
    nx.draw_networkx_edges(G, pos, edgelist=other_edges, edge_color='#94a3b8', width=2, style='dashed')
    
    # Draw path edges
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='#ec4899', width=4)
    
    # Labels
    nx.draw_networkx_labels(G, pos, font_color='white', font_size=12, font_weight='bold')
    
    # Edge weights
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='#94a3b8')
    
    plt.title('A* Optimal Path: A → C → F → G (Lab 5)', fontsize=16, pad=20, color='#f1f5f9')
    plt.axis('off')
    
    plt.savefig('visualizations/lab05_astar_path.png', bbox_inches='tight', dpi=300, facecolor='#0f172a')
    plt.close()

def visualize_lab5_hill_climbing():
    print("Generating Lab 5 Hill Climbing visualization...")
    x = np.linspace(-2, 8, 100)
    y = -(x - 3)**2 + 10
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='#6366f1', linewidth=3, label='Objective Function')
    
    # Highlight peak
    plt.plot(3, 10, 'o', color='#ec4899', markersize=12, label='Global Maximum (3, 10)')
    
    # Highlight start point (example)
    start_x = -1
    start_y = -(start_x - 3)**2 + 10
    plt.plot(start_x, start_y, 'o', color='#8b5cf6', markersize=10, label='Start Point')
    
    # Draw arrow
    plt.annotate('Climbing Direction', xy=(2.8, 9.8), xytext=(0, 5),
                arrowprops=dict(facecolor='#f1f5f9', shrink=0.05),
                color='#f1f5f9', fontsize=10)
    
    plt.title('Hill Climbing Optimization (Lab 5)', fontsize=16, pad=20, color='#f1f5f9')
    plt.xlabel('x', fontsize=12)
    plt.ylabel('f(x) = -(x-3)² + 10', fontsize=12)
    plt.legend(facecolor='#1e293b', edgecolor='#334155', labelcolor='#f1f5f9')
    plt.grid(True, linestyle='--', alpha=0.2)
    
    plt.savefig('visualizations/lab05_hill_climbing.png', bbox_inches='tight', dpi=300)
    plt.close()

if __name__ == "__main__":
    set_style()
    visualize_lab3_data()
    visualize_lab4_graph()
    visualize_lab5_astar()
    visualize_lab5_hill_climbing()
    print("All visualizations generated successfully in 'visualizations/' directory!")
