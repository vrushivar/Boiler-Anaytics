#PCA function
#Y will be target variable
def P_C_A (str):
    x=df.drop([Y], axis=1, inplace=False)
    y=np.array(df[Y])
    nc=12
    pca = PCA(n_components=nc)
    fit = pca.fit(x)
    #print("Explained Variance:",fit.explained_variance_ratio_)
    plt.figure(figsize=(2,2))
    plt.plot(np.cumsum(pca.explained_variance_ratio_),color='m')
    plt.xlim(-2,5)
    plt.title(Y)
    plt.xlabel('Number of components ')
    plt.ylabel('Cumulative explained variance')

    model = PCA(n_components=nc).fit(x)
    X_pc = model.transform(x)
    n_pcs= model.components_.shape[0]
    most_important = [np.abs(model.components_[i]).argmax() for i in range(n_pcs)]
    initial_feature_names = x.columns

    ldf=[]
    for i in most_important:
        if initial_feature_names[i] not in ldf:
            ldf.append(initial_feature_names[i])
    print(ldf)
