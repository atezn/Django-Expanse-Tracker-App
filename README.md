# Django Expense Tracker

## Overview
The Django Expense Tracker is a web application designed to help users track their expenses. It provides a user-friendly interface to visualize expenses using pie charts and manage expense data through an admin interface.

## Features
- Track expenses by category
- Visualize expenses using pie charts
- Manage expenses through the Django admin interface
- Import expense data from an Excel file


## Setup Instructions

### Prerequisites
- Python 3.x
- Django 3.x or higher
- Pandas library

### Installation
- Clone the repository:
   ```bash
   git clone https://github.com/atezn/django-expense-tracker.git
   cd django-expense-tracker

- Create a virtual environment and activate it:
  python -m venv venv
  venv/bin/activate  # On Windows use `venv\Scripts\activate`

- Run the development server:
  ```bash
  cd tracker
  py manage.py runserver

- Open your browser and navigate to http://127.0.0.1:8000 to view the homepage.

## Usage

### Importing Data
- To import expense data from an Excel file(which named 'books.xlx'), place your Excel file in the Source Files directory and run the import script `python tracker/posts/import_data.py`

### Viewing Expenses
- The homepage displays a pie chart of expenses by category.
- The admin interface allows you to manage expenses. Access it at http://127.0.0.1:8000/admin.


