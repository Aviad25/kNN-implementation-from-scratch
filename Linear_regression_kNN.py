import numpy as np
from collections import Counter

#השלד של האלגוריתם 
# מתכוון  לממש גם רגרסיה וגם קלאסיפיקציה 
# Object orriented constructor on python
class CustomKNN:
    def __init__(self,k=3,task_type='regression'):
        self.k = k
        self.task_type = task_type
        # משתנים לשמירת הדאטה
        #כי KNN הוא LAZY LEARNER
        self.x_train = None
        self.y_train = None
            
            
    # פונקציית האימון למרות שאין בכלל אימון ב
    #kNN        
    # רק בשביל התרגול!!!
    def fit(self, X, y):
        # המרה ושמירה של הנתונים ב
        # NUMPY ARRAYS
        # ליתר בטחון
        self.X_train = np.array(X)
        self.y_train = np.array(y)    
        
    #הליבה CORE
    #זה הלב של האלגוריתם. כאן אנחנו מממשים את הנוסחאות עליהן דיברנו
    #הפונקציה תקבל נקודה חדשה X
    #ותקבל את ה Y המשוער שלה 
    
    
    #הלוגיקה 
    #חשב את המרחקים בTRAIN וקח את ה
    # K הכי קרובים 
    #שלוף את הY של השכנים האלו
    #בצע חישוב ממוצע שזה רגרסיה או רוב שזה הקלאסיפיקציה לפי סוג המשימה 
    
    
    def _predict_single(self,x):
        #חישוב מרחק אוקלידי לכל הנקודות בבת אחת (וקטוריזציה)
        #הנוסחה: שורש של סכום הריבועים של ההפרשים
        # זאת פשוט הנוסחא של הרגרסיה
        # של למצוא את הממוצע האידיאלי בהתחשב בכל הנקודות
        distances = np.sqrt(np.sum((self.X_train - x)**2, axis=1))
        # מציאת האינדקסים של 
        # K
        # המרחקים הקצרים ביותר
        # ואז 
        # argsoft
        # מחזיר את האינדקסים שהיו ממיינים את המערך
        # לפי מי הכי קרוב עד ההכי רחוק
        # זה בשביל הקלאסיפיקציה
        k_indices = np.argsort(distances)[:self.k]
        
        # שליפת הערכים (LABELS/VALUES) 
        # של השכנים הכי קרובים
        
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        # ועכשיו שלב הבחירה אם 
        # רגרסיה/קלאסיפיקציה
        # בהתאם לצרכים שלנו
        
        if self.task_type == 'regression':
            return np.mean(k_nearest_labels)
        
        
        elif self.task_type == 'classification':
            #מחזירים את הקלאסיפיקציה של הרוב הכי קרוב 
            #majority vote
            
            most_common = Counter(k_nearest_labels).most_common(1)
            return most_common[0][0]
        
                
    
    # זו הפונקציה שמקבלת רשימה של נקודות
    # ומריצה עליהן את הלוגיקה 
    # שיצרנו בפוקציה למעלה 
    # על כל אחת מהן 
    
    
    def predict(self,X_test) :
        X_test = np.array(X_test)
        #הרצת החיזוי על כל שורה ב
        #TEST SET
        prediction = [self._predict_single(x) for x in X_test]
        return np.array(prediction)
    
         
    
        
        
        
        
# מזל טוב יש לנו את הכל על מנת לחשב כל 
# x , y


# למטה קיימת דוגמה לרגרסיה 
# בסגנון של 
# HARVARDX
# על מנת לבדוק את מה שיצרנו        


#ה X
# יהיה התקציב שלנו כמו בהסברים שלהם בהרוורד
X_train_reg = [[10] , [20] , [30] ,[40] , [50]]
#ה Y
# יהיה המכירות שלהם
y_train_reg = [100 , 200 , 300 , 400 , 500]

# עכשיו נמשוך למטה את הפונקציה של הרגרסיה 

knn_reg = CustomKNN(k=2 , task_type='regression')
knn_reg.fit(X_train_reg , y_train_reg)

# נתון חדש לבדיקה X 
new_budget = [[25]]
# כאן נגלה מה
#הY
#שלו 
prediction = knn_reg.predict(new_budget)
print(f"Regression prediction for {new_budget}: {prediction}")
# הציפייה ש
# שהממוצע שהכי קרוב ל25
# הוא 20 וגם 30
# וצריך לצאת 250


# קלאסיפיקציה  
# דוגמה לסיווג (0 = חתול , 1 = כלב)

X_train_clf = [[1,2],[2,3],[10,10],[11,12]]
y_train_clf = [0,0,1,1]


knn_clf  = CustomKNN(k=3, task_type='classification')
knn_clf.fit(X_train_clf,y_train_clf)



new_animal = [[9,9]]
prediction_clf = knn_clf.predict(new_animal)
print(f"Classification Prediction for {new_animal}: {prediction_clf} ")
# ציפייה
# מכיוון ש [9,9]
# יותר קרוב ל
# [10,10]
# [11,12]

