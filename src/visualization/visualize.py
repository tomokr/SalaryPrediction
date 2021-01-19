import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def cat_boxplot_and_count(df, target, feature):
    df_feature_mean = df.groupby([feature],as_index=False).mean()
    df_feature_sorted = df_feature_mean.sort_values(by=target)
    fig, (ax1, ax2) = plt.subplots(ncols=2)
    fig.set_size_inches(11, 4)
    sns.boxplot(x=feature, y=target, data=df, order=df_feature_sorted[feature].values, ax=ax1)
    ax1.tick_params('x', labelrotation=45)
    sns.countplot(x=feature, data=df, order=df_feature_sorted[feature].values, ax=ax2)
    ax2.tick_params('x', labelrotation=45)
    plt.subplots_adjust(wspace=0.4)

def cat_boxplot(df, target, feature):
    df_feature_mean = df.groupby([feature],as_index=False).mean()
    df_feature_sorted = df_feature_mean.sort_values(by=target)
    plt.figure()
    sns.boxplot(x=feature, y=target, data=df, order=df_feature_sorted[feature].values)
    plt.xticks(rotation=45)

def sorted_pivot(df, target, feature1, feature2):
	pivot = pd.pivot_table(df, index=[feature1], columns = [feature2],values=[target], fill_value=0)
	pivot = pivot.reindex(pivot[target].sort_values(by=pivot.columns[0][1], ascending=False).index)
	display(pivot)
	fig, ax = plt.subplots()
	im = ax.pcolor(pivot[target], cmap='RdBu')

	#label names
	row_labels = pivot[target].columns
	col_labels = pivot[target].index

	#move ticks and labels to the center
	ax.set_xticks(np.arange(pivot[target].shape[1]) + 0.5, minor=False)
	ax.set_yticks(np.arange(pivot[target].shape[0]) + 0.5, minor=False)

	#insert labels
	ax.set_xticklabels(row_labels, minor=False)
	ax.set_yticklabels(col_labels, minor=False)

	#rotate label if too long
	plt.xticks(rotation=90)

	fig.colorbar(im)
	plt.show()
	return None