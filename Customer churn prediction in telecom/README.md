# Прогнозирование оттока клиентов

## Описание проекта

Оператор связи хочет научиться прогнозировать отток клиентов. Если выяснится, что пользователь планирует уйти, ему будут предложены промокоды и специальные условия. Команда оператора собрала персональные данные о некоторых клиентах, информацию об их тарифах и договорах.

## Навыки и инструменты

- python
- pandas
- seaborn
- numpy
- phik
- matplotlib.pyplot
- sklearn.model_selection.train_test_split
- sklearn.compose.ColumnTransformer
- sklearn.preprocessing.StandardScaler
- sklearn.preprocessing.OneHotEncoder
- sklearn.pipeline.Pipeline
- sklearn.model_selection.GridSearchCV
- sklearn.tree.DecisionTreeClassifier
- sklearn.ensemble.RandomForestClassifier
- catboost.CatBoostClassifier
- sklearn.metrics.roc_auc_score
- sklearn.metrics.import.roc_curve
- sklearn.metrics.auc


## Общий вывод

В процессе выполнения проекта: 
 - проведена предобработка данных;
 - проведен исследовательский анализ данных;
 - обучены модели на кросс-валидации:
   - решающее дерево (DecisionTreeClassifier);
   - случайный лес (RandomForestClassifier);
   - градиентный бустинг (CatBoostClassifier).
 - выбранная к использованию модель (CatBoostClassifier), протестирована.
 
 Результаты тестрирования показали, что модель удовлетворяет выдвинутым требованиям.
