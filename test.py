import numpy as np

x = np.array([[1, 2], [3, 4], [5,6]])

for i in np.arange(2):
    x
    
            #                for a in np.arange(self.nbins_total):
            #                    print a
            #                    for b in np.arange(self.nbins_total):
            #                        print b
            #                        for y in np.arange(self.nbins_total):
            #                            print y 
            #                            for z in np.arange(self.nbins_total):
            #                                print z
            #                                self.fshr_l[i,j,l]=self.fsky*(ell+0.5)*(dcl1[a,b]*((cl_t[a,z]*cl_t[b,y]+cl_t[a,y]*cl_t[b,z])**(-1))*dcl2[y,z])
            
            for lb in np.arange((self.lmax+1)/NLB) :
                for ib in np.arange(NLB) :
                    l=lb*NLB+ib
                    if l==0 :
                        continue
                    ell=float(l)
                    indices=np.where((lmin_arr<=l) & (lmax_arr>=l))[0]
                    cl_fid=self.cl_fid_arr[lb,indices,:][:,indices]
                    cl_noise=self.cl_noise_arr[lb,indices,:][:,indices]
                    icl=np.linalg.inv(cl_fid+cl_noise)
                    #print "WHAT IS INDICES??", indices
                    #print self.cl_fid_arr[lb,indices,:]
                    #print self.cl_fid_arr[lb,indices,:][:,indices]
                    for i in np.arange(self.npar_vary+self.npar_mbias) :
                        dcl1=self.dcl_arr[i,lb,indices,:][:,indices]
                        print dcl1
                        for j in np.arange(self.npar_vary-i+self.npar_mbias)+i :
                            dcl2=self.dcl_arr[j,lb,indices,:][:,indices]
                            print dcl2
                            self.fshr_l[i,j,l]=self.fsky*(ell+0.5)*np.trace(np.dot(dcl1,
                                                                                   np.dot(icl,
                                                                                          np.dot(dcl2,
                                                                                                 icl))))
                            if i!=j :
                                self.fshr_l[j,i,l]=self.fshr_l[i,j,l]