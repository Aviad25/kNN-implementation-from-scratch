import math

#אנחנו בודקים אלגוריתם מסחר שעשינו לו 
#BACKTEST
#וקיבלנו ממנו תוצאות
#actual price is the REAL PRICE :  
# the PRICE that the market went to at the end .
#Predicted price is the TP of the algorithm that was predicted 
# by the algo automatically .


# *** Error = Bias^2 + Variance + Irreducible Error ***




actual_prices = [2005.0, 2010.0, 2008.0, 2015.0, 2020.0]


predicted_prices = [2004.0, 2012.0, 2008.0, 2000.0, 2019.0]




# --- CALCULATE RESIDUALS ---


residuals = [] # list
for i in range (len(actual_prices)):
    #residual = actual - predicted
    error = actual_prices[i] - predicted_prices[i]
    residuals.append(error)
    
    print(f"Residuals (Differences) : {residuals}")
    # Result: [1.0, -2.0, 0.0, 15.0, 1.0]
    
    
    
    
    
#  --- IMPLEMENTING THE METRICS ---


def calculate_max_absolute_error(residuals):
    # ימצא  לנו את ההפרש הכי גדול בין איפה שה
    # TAKE PROFIT 
    # היה לבין איפה שהמחיר הגיע בפועל 
    # Find the biggest mistake (absolute value)
    absolute_errors = [abs(e) for e in residuals]
    return max(absolute_errors)
    


def calculate_aae(residuals):
    # ימצא את הממוצע של  כל ההפרשים 
    # יתרון : מספר 1 
    #חסרון : BIAS
    #Average of absolute errors
    absolute_errors = [abs(e) for e in  residuals] # List of all errors
    return sum(absolute_errors) / len(absolute_errors) # average of them


def calculate_Mean_Squared_Error(residuals):
    #היתרונות שלו:
    #1.
    # ענישה לא פרופורציונלית***: בגלל ההעלאה בריבוע***
    #  טעות של 2 הופכת ל-4, 
    # אבל טעות של 10 הופכת ל-100. זה גורם למודל "לפחד"
    # מטעויות גדולות ולנסות לתקן אותן בעדיפות עליונה.
    #2.
    # ביטול סימנים***: השאריות ***
    # (residuals)
    # יכולות להיות חיוביות או שליליות. 
    # ללא הריבוע , הן היו מבטלות זו את זו
    # (למשל, טעות של 5- וטעות של 5+ היו נותנות ממוצע 0,
    # כאילו המודל מושלם).     
    # MSE  :
    # הוא למעשה המדד שמנסה לסכם את שניהם.
    # כשאתה מבצע אופטימיזציה
    #לMSE
    #   אני מנסה למצוא את "נקודת הזהב" שבה גם
    #BIAS & VARIANCE IS LOW AS POSSIBLE
    # כדי שהשגיאה הכוללת תהיה מינימלית 
    squared_errors = [e**2 for e in residuals]
    return sum(squared_errors) / len(squared_errors) 



def calculate_Root_Mean_Squared_Error(residuals):
    
    
    #יתרונות
    #1.
    #אינטואיטיביות: 
    # קל להבין את גודל הטעות הממוצעת ביחידות
    # המקוריות של הנתונים.
    #2.
    # ענישה על חריגים: 
    # הוא שומר על התכונה של ה
    # MSE  
    # הוא עדיין מושפע מאוד מטעויות גדולות 
    # (כי הריבוע קורה לפני השורש).
    
    
    squared_errors = [e**2 for e in residuals]
    mse = sum(squared_errors) / len(squared_errors)
    return math.sqrt(mse)



def calculate_model_bias(residuals):
    # Mean Error without Absolute or Square
    # positive = model is underestimating (Target is too low)
    # negative = model is overestimating (Target is too high)
    # ממוצע קלאסי בשביל BIAS
    return sum(residuals) / len(residuals)








max_err = calculate_max_absolute_error(residuals)
mae = calculate_aae(residuals)
mse = calculate_Mean_Squared_Error(residuals)
rmse = calculate_Root_Mean_Squared_Error(residuals)
bias = calculate_model_bias(residuals)




print(f"Max Absolute Error: {max_err} (Worst trade missed by $15)")
print(f"MAE: {mae} (Average miss is $3.8)")
print(f"MSE: {mse} (High because of the squared 15)")
print(f"RMSE: {rmse} (Standard deviation of error)")
print(f"Model Bias: {bias} (On average, we are under/over shooting by this much)")


# --- TERMINAL ---


#Residuals (Differences) : [1.0]
#Residuals (Differences) : [1.0, -2.0]
#Residuals (Differences) : [1.0, -2.0, 0.0]
#Residuals (Differences) : [1.0, -2.0, 0.0, 15.0]     
#Residuals (Differences) : [1.0, -2.0, 0.0, 15.0, 1.0]
#Max Absolute Error: 15.0 (Worst trade missed by $15) 
#MAE: 3.8 (Average miss is $3.8)
#MSE: 46.2 (High because of the squared 15)
#RMSE: 6.797058187186572 (Standard deviation of error)
#Model Bias: 3.0 
#(On average, we are under/over shooting by this much)  