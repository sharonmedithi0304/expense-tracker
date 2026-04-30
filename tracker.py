import pandas as pd
import os
from datetime import datetime

FILE_PATH = 'data/expenses.csv'

def load_data():
    if os.path.exists(FILE_PATH):
        return pd.read_csv(FILE_PATH)
    else:
        df = pd.DataFrame(columns=['ID', 'Date', 'Category', 'Amount', 'Description'])
        df.to_csv(FILE_PATH, index=False)
        return df

def save_data(df):
    df.to_csv(FILE_PATH, index=False)

def add_expense(category, amount, description):
    df = load_data()
    new_id = 1 if len(df) == 0 else int(df['ID'].max()) + 1
    today = datetime.now().strftime('%Y-%m-%d')
    new_row = {
        'ID': new_id,
        'Date': today,
        'Category': category.capitalize(),
        'Amount': float(amount),
        'Description': description
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df)
    print(f"\n✅ Expense added! ID: {new_id}")

def view_expenses():
    df = load_data()
    if len(df) == 0:
        print("\n⚠️  No expenses found.")
        return
    print("\n" + "=" * 65)
    print(f"{'ID':<5} {'Date':<12} {'Category':<15} {'Amount':>10} {'Description'}")
    print("=" * 65)
    for _, row in df.iterrows():
        print(f"{int(row['ID']):<5} {row['Date']:<12} {row['Category']:<15} Rs.{row['Amount']:>9.2f} {row['Description']}")
    print("=" * 65)
    print(f"{'TOTAL':>33} Rs.{df['Amount'].sum():>9.2f}")
    print("=" * 65)

def category_summary():
    df = load_data()
    if len(df) == 0:
        print("\n⚠️  No expenses found.")
        return
    summary = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    print("\n" + "=" * 35)
    print(f"  CATEGORY-WISE SUMMARY")
    print("=" * 35)
    for category, total in summary.items():
        print(f"  {category:<20} Rs.{total:>8.2f}")
    print("=" * 35)
    print(f"  {'TOTAL':<20} Rs.{df['Amount'].sum():>8.2f}")
    print("=" * 35)

def delete_expense(expense_id):
    df = load_data()
    if expense_id not in df['ID'].values:
        print(f"\n❌ No expense found with ID {expense_id}")
        return
    df = df[df['ID'] != expense_id]
    save_data(df)
    print(f"\n✅ Expense {expense_id} deleted.")