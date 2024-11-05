import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def load_data(entity_file, relation_file, triple_file):
    # 读取实体编号
    with open(entity_file, 'r') as f:
        entity_count = int(f.readline().strip())
        entities = {line.split()[0]: int(line.split()[1]) for line in f}

    # 读取关系编号
    with open(relation_file, 'r') as f:
        relation_count = int(f.readline().strip())
        relations = {line.split()[0]: int(line.split()[1]) for line in f}

    # 逐行读取三元组以节省内存
    triples = []
    with open(triple_file, 'r') as f:
        triple_count = int(f.readline().strip())
        for line in f:
            head, tail, _ = map(int, line.split())
            triples.append((head, tail))  # 只保留头和尾实体编号

    return entities, relations, triples


def create_graph(triples):
    G = nx.MultiGraph()  # 使用多重图来考虑重边和回路
    G.add_edges_from(triples)
    return G


def analyze_graph(G):
    # 统计图的基本信息
    print(f"节点数量: {G.number_of_nodes()}")
    print(f"边数量: {G.number_of_edges()}")

    # 节点度分布
    degree_sequence = np.array([G.degree(n) for n in G.nodes()])

    # 获取最大的连通分量
    largest_component = max(nx.connected_components(G), key=len)
    G_largest = G.subgraph(largest_component)

    # 最短路径长度分布：限制计算范围
    path_lengths = []
    for node in G_largest.nodes():
        try:
            lengths = nx.single_source_shortest_path_length(G_largest, node)
            path_lengths.extend(lengths.values())
        except MemoryError:
            print("内存不足，无法计算最短路径长度")
            break

    # 节点聚类系数分布
    clustering_coeffs = list(nx.clustering(G_largest).values())

    # k-shell 分布
    k_shell = list(nx.core_number(G_largest).values())

    return degree_sequence, path_lengths, clustering_coeffs, k_shell, largest_component


def plot_distribution(data, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, alpha=0.7, color='b', edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


def main():
    # 文件路径
    entity_file = r"C:\Users\23253\Downloads\数据集\PMM-期末综合设计-数据集-ToS\A-复杂网络\FB15K237-NET\entity2id.txt"
    relation_file = r"C:\Users\23253\Downloads\数据集\PMM-期末综合设计-数据集-ToS\A-复杂网络\FB15K237-NET\relation2id.txt"
    triple_file = r"C:\Users\23253\Downloads\数据集\PMM-期末综合设计-数据集-ToS\A-复杂网络\FB15K237-NET\all_triple.txt"

    # 加载数据
    entities, relations, triples = load_data(entity_file, relation_file, triple_file)

    # 创建图
    G = create_graph(triples)

    # 分析图
    degree_sequence, path_lengths, clustering_coeffs, k_shell, largest_component = analyze_graph(G)

    # 绘制分布图
    plot_distribution(degree_sequence, '节点度分布', '节点度', '频率')
    plot_distribution(path_lengths, '最短路径长度分布', '路径长度', '频率')
    plot_distribution(clustering_coeffs, '节点聚类系数分布', '聚类系数', '频率')
    plot_distribution(k_shell, '节点 k-shell 分布', 'k-shell 值', '频率')

    # 计算均值和方差
    print("节点度均值:", np.mean(degree_sequence), "方差:", np.var(degree_sequence))
    print("最短路径长度均值:", np.mean(path_lengths), "方差:", np.var(path_lengths))
    print("聚类系数均值:", np.mean(clustering_coeffs), "方差:", np.var(clustering_coeffs))
    print("k-shell均值:", np.mean(k_shell), "方差:", np.var(k_shell))

    # 打印最大连通子图的信息
    print(f"最大连通子图的节点数量: {len(largest_component)}")
    print(f"最大连通子图的边数量: {G.subgraph(largest_component).number_of_edges()}")


if __name__ == "__main__":
    main()
