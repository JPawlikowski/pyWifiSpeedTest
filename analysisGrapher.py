import matplotlib.pyplot as plt


def analysisGrapherFunc(x_vals, y_vals, graph_name, current_time):
    current_file = str("./graphs/" + graph_name + "_" + current_time +  ".png")
    fig, ax = plt.subplots()
    ax.set_xlabel('dates (YYYY-MM)')
    if (graph_name.lower() == 'pings'):
        ax.set_ylabel(graph_name + ' (ms)')
    else:
        ax.set_ylabel(graph_name + ' (Mbps)')

    #plt.plot(x_vals, y_vals)
    plt.scatter(x_vals, y_vals)
    plt.xticks(fontsize=8)
    plt.xticks(rotation=70)
    plt.tight_layout()

    plt.savefig(current_file, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', format=None, transparent=False, bbox_inches=None, pad_inches=0.1,  metadata=None)
    print("Graph created : " + current_file)

