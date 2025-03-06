import os
import django
import pandas as pd
from decimal import Decimal
from django.db.models import Sum

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tracker.settings')
django.setup()

from posts.models import Book

def import_books():
    df = pd.read_excel('tracker\Source Files\\books.xlsx')
    
    for _, row in df.iterrows():
        #published_date = pd.to_datetime(row['published_date'], errors='coerce')

        Book.objects.create(
                    title=row['title'],
                    category=row['category'],
                    author=row['authors'],
                    distribution_expense=Decimal(str(row['distribution_expense'])),
                    #date= published_date
                )


def expenses_by_category():
    expenses = Book.objects.values('category').annotate(total_expense=Sum('distribution_expense'))
    return {
        'labels': [expense['category'] for expense in expenses],
        'data': [float(expense['total_expense']) for expense in expenses]
    }
    
if __name__ == '__main__':
    
    #importt_books() # Uncomment this line to import books from excel file
    print(expenses_by_category())
