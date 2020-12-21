#!/usr/bin/env python3

import numpy

class sim_net():
    def __init__(self,N,P,prob,H,gamma,normalize):
        self.initialize(N,P,prob,H,gamma,normalize)

    def _step(self,z):
        return 0.5*numpy.sign(z)+0.5

    def _set_weight(self,a):
        if self.norm_mode=="sym":
            self.W=a*self.Wauto+self.Whetero-(a+1)*self.WG
        elif self.norm_mode=="asym":
            self.W=a*self.Wauto+self.Whetero-(a+1)*self.WG

    def initialize(self,N,P,prob,H,gamma,normalize):
        self.N=N
        self.P=P
        self.prob=prob
        self.H=H
        self.gamma=gamma
        self.V=self.prob*(1-self.prob)
        self.norm_mode=normalize
        #normalization
        if self.norm_mode=="sym":
            Dnorm=numpy.diag(numpy.sum(self.H,axis=1)**-0.5)
            self.H=Dnorm@self.H@Dnorm
        elif self.norm_mode=="asym":
            Dnorm=numpy.diag(numpy.sum(self.H,axis=1)**-1)
            self.H=Dnorm@self.H
        else:
            print("Error: Normalization mode sym or asym was not specified.")
            exit()
        #generate patterns
        self.xi=(numpy.random.rand(self.N,self.P)<self.prob).astype(numpy.float)
        self.xi_mean=numpy.sum(self.xi, axis=1, keepdims=True)/self.P
        self.xi_bias=self.xi-self.xi_mean
        #weights
        if self.norm_mode=="sym":
            self.Wauto=(self.xi_bias@self.xi_bias.T)/(self.N*self.V)
            self.Whetero=(self.xi_bias@self.H@self.xi_bias.T)/(self.N*self.V)
            self.WG=self.gamma/self.N
        elif self.norm_mode=="asym":
            self.Wauto=(self.xi@self.xi.T)/(self.N*self.V)
            self.Whetero=(self.xi@self.H@self.xi.T)/(self.N*self.V)
            self.WG=self.P*self.xi_mean@self.xi_mean.T/(self.N*self.V)+self.gamma/self.N

    def simulate_single(self,a,eta,simlen,start_node,energycheck=True):
        self._set_weight(a)
        #simulation
        self.x=self.xi[:,start_node]+0.0
        self.m_log=numpy.zeros([simlen,self.P])
        self.obj_log=numpy.zeros([simlen])
        for t in range(simlen):
            if t%100==0:
                print(t)
            self.r=self._step(self.W@self.x)
            self.x+=eta*(self.r-self.x)
            self.m=(self.xi_bias.T@self.x)/(self.N*self.V)
            self.m_log[t,:]=self.m
            if energycheck:
                self.obj_log[t]=-(self.x).T@self.W@self.x/(self.N*self.V)

        return (self.m_log, self.obj_log)

    def simulate_allstarts(self,a,eta,simlen):
        self._set_weight(a)
        #simulation
        self.x=self.xi+0.0
        self.m_log=numpy.zeros([simlen,self.P,self.P])
        for t in range(simlen):
            if t%100==0:
                print(t)
            self.r=self._step(self.W@self.x)
            self.x+=eta*(self.r-self.x)
            self.m=(self.xi_bias.T@self.x)/(self.N*self.V)
            self.m_log[t,:,:]=self.m

        #correlation between attractors
        self.cor_activity=numpy.corrcoef(self.x.T)

        return (self.m_log, self.cor_activity)

    """
    def simulate_single_changeparam_slowinh(self,a_array,eta,simlen,start_node,etaslow,Uslow,noise_amp):
        if len(a_array)!=simlen:
            print("Error: length of a_array must be matched to simlen.")
            exit()
        #simulation
        self.x=self.xi[:,start_node]+0.0
        self.m_log=numpy.zeros([simlen,self.P])
        self.y=numpy.zeros_like(self.x)
        for t in range(simlen):
            a=a_array[t]
            if t%100==0:
                print(t,a)
            self._set_weight(a)
            self.r=self._step(self.J@self.x-Uslow*(a+1)*self.y)
            self.x+=eta*(self.r-self.x+noise_amp*numpy.random.randn(self.N))
            self.y+=etaslow*(self.r-self.y)
            self.m=(self.xi.T@self.x)/(self.N*self.prob)
            self.m_log[t,:]=self.m

        return self.m_log

    def simulate_single_feedback_slowinh(self,target_arr,eta,simlen,start_node,etaslow,Uslow,noise_amp, max_a, min_a):
        if len(target_arr)!=simlen:
            print("Error: length of a_array must be matched to simlen.")
            exit()
        #simulation
        self.x=self.xi[:,start_node]+0.0
        match=0.0
        self.m_log=numpy.zeros([simlen,self.P])
        self.y=numpy.zeros_like(self.x)
        for t in range(simlen):
            a=(max_a-min_a)*match+min_a
            if t%100==0:
                print(t,a)
            self._set_weight(a)
            self.r=self._step(self.J@self.x-Uslow*self.y)
            self.x+=eta*(self.r-self.x+noise_amp*numpy.random.randn(self.N))
            self.y+=etaslow*(self.r-self.y)
            self.m=(self.xi.T@self.x)/(self.N*self.prob)
            match=numpy.max([self.m[target_arr[t]],0])
            self.m_log[t,:]=self.m

        return self.m_log
    """
