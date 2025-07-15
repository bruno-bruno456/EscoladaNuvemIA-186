from sklearn.datasets import load_breast_cancer # Dataset do CA de mama
from sklearn.ensemble import RandomForestClassifier # Algoritmo do Random Forest

# Métricas para avaliação do modelo
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

# Função para dividir o dataset
from sklearn.model_selection import train_test_split


data = load_breast_cancer()

"""
O dataset contém características (data.data) e rótulos (data.target)
data.data: matriz com 30 características para cada amostra.
data.target: vetor com 0 (maligno) ou 1 (benigno) para cada amostra.

Dataset contém 569 amostras.
Divisão dos dados: 70% para treino e 30% para teste
X_train e X_test: características para treino e teste
y_train e y_test: rótulos para treino e para teste

random_state=42: garantir a reprodutibilidade dos resultados
"""

X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=42)

# Iniciando o modelo com os parâmetros padrão
model = RandomForestClassifier()

# Treinar o modelo com os dados de treinamento
model.fit(X_train, y_train)

# Fazendo as previsões com os dados de teste
y_prep = model.predict(X_test) # Previsões de classe 0 ou 1
y_prep_proba = model.predict_proba(X_test)[:,1] # Probabilidade de ser de classe 1


precision = precision_score(y_test, y_prep) # Precisão: TP / (TP + FP)
recall = recall_score(y_test, y_prep) # Sensibilidade: TP / (TP + FN)
f1 = f1_score(y_test, y_prep) # F1: 2*((precision * recall)/(precision + recall))
auc = roc_auc_score(y_test, y_prep_proba) # Área sob a curva ROC

print(f"""
Precisão: {precision:.2f} 
Recall: {recall:.2f}
F1-Score: {f1:.2f}
AUC-ROC: {auc:.2f}
""")

# Precisão alta = baixo número de falsos positivos
# Recall alto = baixo número de falsos negativos
# F1 alto = Equilibrio entre as métricas Precision e Recall
# AUC-ROC alto = Boa dricriminação entre as classes do modelo