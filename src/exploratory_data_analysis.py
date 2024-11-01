import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def data_overview(df, num_rows=5):
    """
    データフレームの概観を表示する関数。

    引数:
    df : pandas.DataFrame
        概観を表示するデータフレーム。
    num_rows : int, オプション
        表示する最初の行数。デフォルトは5行。

    出力:
    データフレームのサイズ、各列のデータ型、最初の数行、欠損値の数、
    基本的な統計情報をコンソールに表示します。
    """
    print("データフレームのサイズ:", df.shape)
    print("\n各列のデータ型:\n", df.dtypes)
    print(f"\n最初の{num_rows}行:\n", df.head(num_rows))
    print("\n欠損値の数:\n", df.isnull().sum())
    print("\n基本的な統計情報:\n", df.describe(include='all'))

def plot_heatmap(df, cat_var1, cat_var2, font_path='../data/ipaexg.ttf', show_percentage=False, title=None):
    """
    質的変数間の関係性をヒートマップで可視化する関数。

    引数:
    df : pandas.DataFrame
        データフレーム。
    cat_var1 : str
        質的変数1の列名。
    cat_var2 : str
        質的変数2の列名。
    font_path : str, オプション
        日本語フォントのファイルパス。デフォルトは '../ipaexg.ttf'。
    show_percentage : bool, オプション
        Trueの場合、行ごとの割合を表示します。デフォルトは False。
    title : str, オプション
        ヒートマップのタイトル。デフォルトは None（自動生成タイトル）。

    出力:
    ヒートマップを表示します。
    """
    # フォントを登録
    fm.fontManager.addfont(font_path)
    plt.rcParams['font.family'] = 'IPAexGothic'  # フォントファミリを設定

    # クロス集計を作成
    contingency_table = pd.crosstab(df[cat_var1], df[cat_var2])
    
    # 行ごとの割合を計算する場合
    if show_percentage:
        contingency_table = contingency_table.div(contingency_table.sum(axis=1), axis=0) * 100

    # ヒートマップを描画
    plt.figure(figsize=(10, 6))
    sns.heatmap(contingency_table, annot=True, fmt='.1f' if show_percentage else 'd', cmap='RdYlBu_r', cbar=True)
    
    # タイトルとラベルの設定
    if title is None:  # タイトルが指定されていない場合はデフォルトのタイトルを生成
        title = f'{cat_var1} と {cat_var2} のヒートマップ' + ('（割合）' if show_percentage else '')

    plt.title(title)
    plt.xlabel(cat_var2)
    plt.ylabel(cat_var1)
    
    plt.show()

def plot_boxplot(df, cat_var, num_var, font_path='../data/ipaexg.ttf', title=None):
    """
    質的変数と量的変数の関係性を箱ひげ図で可視化する関数。

    引数:
    df : pandas.DataFrame
        データフレーム。
    cat_var : str
        質的変数の列名。
    num_var : str
        量的変数の列名。
    font_path : str, オプション
        日本語フォントのファイルパス。デフォルトは '../ipaexg.ttf'。
    title : str, オプション
        箱ひげ図のタイトル。デフォルトは None（自動生成タイトル）。

    出力:
    箱ひげ図を表示します。
    """
    # フォントを登録
    fm.fontManager.addfont(font_path)
    plt.rcParams['font.family'] = 'IPAexGothic'  # フォントファミリを設定

    # 箱ひげ図を描画
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=cat_var, y=num_var)

    # グリッドの追加
    plt.grid(True, linestyle='--', alpha=0.7)  # グリッドを表示する

    # タイトルの設定
    if title is None:  # タイトルが指定されていない場合はデフォルトのタイトルを生成
        title = f'{cat_var} と {num_var} の箱ひげ図'

    plt.title(title)
    plt.xlabel(cat_var)
    plt.ylabel(num_var)
    
    plt.show()

