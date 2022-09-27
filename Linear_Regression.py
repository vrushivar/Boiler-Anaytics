#Linear regression function

def LR(str):
    x=df.drop([Y], axis=1, inplace=False)
    y=np.array(df[Y])
    X_train,X_test,y_train,y_test=train_test_split(x,y, test_size=0.3, random_state=30)
    TR=[]
    TE=[]
    model=LinearRegression().fit(X_train,y_train)
    model_Train_pred=model.predict(X_train)
    model_pred=model.predict(X_test)
    errorstr = mean_squared_error(y_train,model_Train_pred)
    errorste = mean_squared_error(y_test, model_pred)
    print("\n")
    print('\033[95m',"**********Accuracy results for Linear regression:",Y,"***********",'\033[0m')
    print('\nrmse(On train,On test)=',(errorstr**0.5,errorste**0.5))
    
    errorstr = mean_absolute_error(y_train,model_Train_pred)
    errorste = mean_absolute_error(y_test, model_pred)
    print('\nmae(On train,On test)=',(errorstr,errorste))
    
    r2tr = r2_score(y_train,model_Train_pred)
    r2te = r2_score(y_test, model_pred)
    TR.append(r2tr)
    TE.append(r2te)
    
    print('\nR2(On train,On test)=',(r2tr,r2te))
