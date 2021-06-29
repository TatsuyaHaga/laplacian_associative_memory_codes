#!/usr/bin/env python3

import numpy
import pylab
import networkx

def get_graph_from_file(edgelist_file):
    return networkx.read_edgelist(edgelist_file, nodetype=int, delimiter=",") 

def get_graph_from_edgelist(edgelist):
    G=networkx.Graph()
    G.add_edges_from(edgelist)
    return G
    
def get_pos_spring(G):
    return networkx.spring_layout(G)

def plot_network(filename, G, pos, title=None):
    pylab.figure(figsize=(4,3))
    nc=networkx.draw_networkx_nodes(G,pos,node_color="black", node_size=50)
    networkx.draw_networkx_edges(G,pos)
    if title!=None:
        pylab.title(title,fontsize=20)
    pylab.axis("off")
    pylab.savefig(filename)
    pylab.close()

def plot_network_big(filename, G, pos, title=None):
    #pylab.figure(figsize=(4,3))
    nc=networkx.draw_networkx_nodes(G,pos,node_color="black", node_size=50)
    networkx.draw_networkx_edges(G,pos)
    if title!=None:
        pylab.title(title,fontsize=20)
    pylab.axis("off")
    pylab.savefig(filename)
    pylab.close()

def plot_network_sizefix(filename, G, pos, figsize, title=None):
    pylab.figure(figsize=figsize)
    nc=networkx.draw_networkx_nodes(G,pos,node_color="black", node_size=50)
    networkx.draw_networkx_edges(G,pos)
    if title!=None:
        pylab.title(title,fontsize=20)
    pylab.axis("off")
    pylab.savefig(filename)
    pylab.close()

def plot_network_asym(filename, G, pos, title=None):
    #pylab.figure(figsize=(6,6))
    nc=networkx.draw_networkx_nodes(G,pos,node_color="black", node_size=100)
    networkx.draw_networkx_edges(G,pos,arrowsize=12)
    if title!=None:
        pylab.title(title,fontsize=20)
    pylab.axis("off")
    pylab.savefig(filename)
    pylab.close()

def plot_network_label(filename, G, pos, title=None):
    pylab.figure(figsize=(4,3))
    nc=networkx.draw(G,pos,with_labels=True)
    if title!=None:
        pylab.title(title,fontsize=20)
    pylab.axis("off")
    pylab.savefig(filename)
    pylab.close()

def plot_color_network(filename, G, pos, color_list, title=None):
    pylab.figure(figsize=(4,3))
    color_list=color_list[G.nodes()]
    color_max=numpy.max([numpy.max(color_list), numpy.abs(numpy.min(color_list))])
    nc=networkx.draw_networkx_nodes(G,pos,node_color=list(color_list),cmap="bwr", vmin=-color_max, vmax=color_max, node_size=50)
    networkx.draw_networkx_edges(G,pos)
    if title!=None:
        pylab.title(title,fontsize=20)
    pylab.axis("off")
    pylab.colorbar(nc)
    pylab.savefig(filename)
    pylab.close()

def plot_color_network_positive(filename, G, pos, color_list, title=None):
    pylab.figure(figsize=(4,3))
    color_list=color_list[G.nodes()]
    color_max=numpy.max([numpy.max(color_list), numpy.abs(numpy.min(color_list))])
    nc=networkx.draw_networkx_nodes(G,pos,node_color=list(color_list),cmap="Reds", vmin=0, vmax=color_max, node_size=50)
    networkx.draw_networkx_edges(G,pos)
    if title!=None:
        pylab.title(title,fontsize=20)
    pylab.axis("off")
    pylab.colorbar(nc)
    pylab.savefig(filename)
    pylab.close()

def plot_color_network_zeroone(filename, G, pos, color_list, title=None):
    pylab.figure(figsize=(4,3))
    color_list=color_list[G.nodes()]
    nc=networkx.draw_networkx_nodes(G,pos,node_color=list(color_list),cmap="Reds", vmin=0, vmax=1, node_size=50)
    networkx.draw_networkx_edges(G,pos)
    if title!=None:
        pylab.title(title,fontsize=20)
    pylab.axis("off")
    pylab.colorbar(nc)
    pylab.savefig(filename)
    pylab.close()

def plot_overlap(filename, m_log):
    pylab.figure(figsize=(4,3))
    pylab.imshow(m_log.T, interpolation="none", aspect="auto")
    pylab.xlabel("Time")
    pylab.ylabel("Pattern")
    pylab.colorbar()
    pylab.tight_layout()
    pylab.savefig(filename)
    pylab.close() 

def plot_overlap_withparam(filename, m_log, param):
    pylab.figure(figsize=(4,4))
    pylab.subplot2grid((3,1),(0,0),rowspan=1)
    pylab.plot(param)
    pylab.xlim([0,len(param)-1])
    pylab.ylabel("a")
    pylab.subplot2grid((3,1),(1,0),rowspan=2)
    pylab.imshow(m_log.T, interpolation="none", aspect="auto", cmap="jet")
    pylab.xlabel("Time")
    pylab.ylabel("Pattern")
    #pylab.colorbar()
    pylab.tight_layout()
    pylab.savefig(filename)
    pylab.colorbar()
    pylab.tight_layout()
    pylab.savefig("colorbar_"+filename)
    pylab.close() 

def plot_overlap_groupsum(filename, m_log, group_id):
    pylab.figure(figsize=(4,3))
    Ngroup=int(numpy.max(group_id)+1)
    for i in range(Ngroup):
        groupsum=numpy.mean(m_log[:,group_id==i],axis=1)
        pylab.plot(groupsum, label="Group "+str(i+1))
    pylab.xlabel("Time")
    pylab.ylabel("Mean overlap")
    pylab.legend()
    pylab.tight_layout()
    pylab.savefig(filename)
    pylab.close() 

def plot_overlap_groupsum_withparam(filename, m_log, group_id, param):
    pylab.figure(figsize=(4,4))
    pylab.subplot2grid((3,1),(0,0),rowspan=1)
    pylab.plot(param)
    pylab.xlim([0,len(param)-1])
    pylab.ylabel("a")
    pylab.subplot2grid((3,1),(1,0),rowspan=2)
    Ngroup=int(numpy.max(group_id)+1)
    for i in range(Ngroup):
        groupsum=numpy.mean(m_log[:,group_id==i],axis=1)
        pylab.plot(groupsum, label="Group "+str(i+1))
    pylab.xlabel("Time")
    pylab.ylabel("Mean overlap")
    pylab.legend()
    pylab.tight_layout()
    pylab.savefig(filename)
    pylab.close()

def plot_pattern_cor(filename, cor, title=None):
    pylab.figure(figsize=(4,3))
    P=cor.shape[0]
    pylab.imshow(cor,interpolation="none",cmap="bwr", vmax=1, vmin=-1, extent=[0.5,P+0.5,P+0.5,0.5])
    pylab.xticks([1,P])
    pylab.yticks([1,P])
    pylab.xlabel("Trigger stimulus",fontsize=12)
    pylab.ylabel("Trigger stimulus",fontsize=12)
    pylab.colorbar()
    if title!=None:
        pylab.title(title, fontsize=20)
    pylab.tight_layout()
    pylab.savefig(filename)
    pylab.close()

def plot_cossim_basis(filename, a_arr, overlaps, eigenvec, eigenval):
    p=eigenvec.shape[1]
    cossim_basis=numpy.zeros([len(a_arr),p])    
    #cosine similarity between gl and attractor
    for a_ind in range(len(a_arr)):
        for i in range(p):
            cossim_basis[a_ind,i]=numpy.abs(numpy.sum(overlaps[a_ind]*eigenvec[:,i]))

    #plot similarity between overlap and bases
    pylab.pcolormesh(numpy.arange(0.5,p+0.5,1.0),a_arr,cossim_basis,cmap="hot")
    pylab.colorbar()
    pylab.plot(numpy.arange(1,p+1),eigenval-1, ".", color="white")
    pylab.savefig(filename)
    pylab.close() 

