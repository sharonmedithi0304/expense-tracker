from tracker import add_expense, view_expenses, category_summary, delete_expense

def main():
    print("=" * 40)
    print("      💰 EXPENSE TRACKER")
    print("=" * 40)
    
    while True:
        print("\nWhat do you want to do?")
        print("  1. Add expense")
        print("  2. View all expenses")
        print("  3. Category summary")
        print("  4. Delete expense")
        print("  5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '1':
            print("\nCategories: Food, Transport, Shopping, Education, Entertainment, Other")
            category = input("Category: ").strip()
            amount = input("Amount (₹): ").strip()
            description = input("Description: ").strip()
            
            # Validate amount — make sure it's a number
            try:
                float(amount)
                add_expense(category, amount, description)
            except ValueError:
                print("❌ Invalid amount. Enter a number.")
        
        elif choice == '2':
            view_expenses()
        
        elif choice == '3':
            category_summary()
        
        elif choice == '4':
            view_expenses()
            expense_id = input("\nEnter ID to delete: ").strip()
            try:
                delete_expense(int(expense_id))
            except ValueError:
                print("❌ Invalid ID.")
        
        elif choice == '5':
            print("\n👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Enter 1-5.")

if __name__ == "__main__":
    main()