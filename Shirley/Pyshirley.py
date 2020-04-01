def remove_shirley(x,y,x_mine,x_maxe,**kwargs):

   
    x_min=int(np.where(x==x_mine)[0])
    x_max=int(np.where(x==x_maxe)[0])

    shir_sum=0
    shir_bkg=[]
    shir_x=[]
    m0=np.sum(y[-5:])/5

    for i in range(x.shape[0],x_max,-1):
        shir_bkg.append(0)
        shir_x.append(x[i-1])

    for i in range(x_max,x_min,-1):
        shir_sum=shir_sum+y[i-1]
        shir_bkg.append(float(shir_sum))
        shir_x.append(x[i-1])

    m1=(np.sum(y[x_min:x_min+5])-np.sum(y[-5:]))/np.sum(shir_bkg[-5:]) 
    shir_bkg=np.multiply(shir_bkg,m1)+m0

    m3=np.sum(shir_bkg[-5:])/5
    for i in range(x_min,0,-1):
        shir_bkg=np.append(shir_bkg,m3)
        shir_x.append(x[i-1])
    
    shir_x=np.flip(shir_x)
    shir_bkg=np.flip(shir_bkg)
    plt.figure()
    plt.plot(shir_x,shir_bkg)
    plt.plot(x,y)
    plt.show()
    area_a=[]    
    area_a.append(np.sum(y)-np.sum(shir_bkg))
    area_a.append(np.sum(y)) 
    area_a.append(np.sum(shir_bkg)) 
    area_a.append(float(np.sum(shir_bkg))/1000/(x.max()-x.min()))
    #print(area_a)
    #shir_y=[]
    shir_y=(y-shir_bkg)/area_a[3]
    plt.figure()
    plt.plot(shir_x,shir_y)
    plt.ylabel('counts/meV')
    plt.show()

    return shir_x,shir_y,shir_bkg,area_a