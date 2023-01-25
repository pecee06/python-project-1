import pandas as pd
import matplotlib.pyplot as plt
import time

#BackEnd
def new_entry():
    book_id = int(input('Enter Book ID : '))
    title = input('Enter Title of Book : ')
    author = input('Enter Author of Book : ')
    publisher =input('Enter Publisher of Book : ')
    edition = input('Enter Edition of Book : ')
    cost = float(input('Enter Cost of Book : '))
    category = input('Enter Category of Book : ')
    bdf = pd.read_csv('Book.csv')
    n = bdf['book_id'].count()
    bdf.at[n] = [book_id,title,author,publisher,edition,cost,category]
    bdf.to_csv('Book.csv',index=False)
    print('Book Added Successfully')
    print(bdf)
    
def search_book():
    title = input('Enter Title of Book : ')
    bdf = pd.read_csv('Book.csv')
    df=bdf.loc[bdf['title']==title]
    if df.empty:
        print('No Book Found')
    else:
        print('Book Details :')
        print(df)
        
def delete_book():
    book_id = int(input('Enter Book ID : '))
    bdf = pd.read_csv('Book.csv')
    bdf = bdf.drop(bdf[bdf['book_id']==book_id].index)
    bdf.to_csv('Book.csv',index=False)
    print('Book Deleted Successfully')
    print(bdf)
    
def show_book():
    bdf = pd.read_csv('Book.csv')
    print(bdf)
    
def new_member():
    m_id = int(input('Enter Member ID : '))
    m_name = input('Enter Name : ')
    phoneNo = input('Enter Phone Number : ')
    mdf = pd.read_csv('Member.csv')
    n = mdf['m_id'].count()
    mdf.at[n] = [m_id,m_name,phoneNo]
    mdf.to_csv('Member.csv',index=False)
    print('New Member Added Successfully')
    print(mdf)
    
def search_member():
    m_name = input('Enter Name : ')
    bdf = pd.read_csv('Member.csv')
    df = bdf.loc[bdf['m_name']==m_name]
    if df.empty:
        print('No Member Found with Given Name')
    else:
        print('Member Details :')
        print(df)
        
def delete_member():
    m_id = int(input('Enter Member ID : '))
    bdf = pd.read_csv('Member.csv')
    bdf = bdf.drop(bdf[bdf['m_id']==m_id].index)
    bdf.to_csv('Member.csv',index=False)
    print('Member Deleted Successfully')
    print(bdf)
    
def show_member():
    bdf = pd.read_csv('Member.csv')
    print(bdf)
    
def issue_book():
    book_name = input('Enter Book Name : ')
    bdf = pd.read_csv('Book.csv')
    bdf = bdf.loc[bdf['title']==book_name]
    if bdf.empty:
        print('No Book Found in the Library')
        return
    m_name = input('Enter Member Name : ')
    mdf = pd.read_csv('Member.csv')
    mdf = mdf.loc[mdf['m_name']==m_name]
    if mdf.empty:
        print('No such Member Found')
        return
    dateofissue = f'{time.ctime()}'
    numberofbooksissued = int(input('Enter Number of Books Issued : '))
    bdf = pd.read_csv('Issuebooks.csv')
    n = bdf['book_name'].count()
    bdf.at[n] = [book_name,m_name,dateofissue,numberofbooksissued]
    bdf.to_csv('Issuebooks.csv',index=False)
    print('Book Issues Successfully')
    print(bdf)
    
def return_book():
    m_name = input('Enter Name : ')
    book_name = input('Enter Book Name : ')
    idf = pd.read_csv('Issuebooks.csv')
    idf= idf.loc[idf['book_name']==book_name]
    if idf.empty:
        print('The Book is not Issued')
    else:
        idf = idf.loc[idf['m_name']==m_name]
        if idf.empty:
            print('The Book is not Issued to the Member')
        else:
            print('Book can be Returned')
            ans = input('Are you sure, you want to return the book : ')
            if ans == 'y':
                idf = pd.read_csv('Issuebooks.csv')
                idf = idf.drop(idf[idf['book_name']==book_name].index)
                idf = idf.to_csv('Issuebooks.csv',index=False)
                print('book Returned Successfully')
            else:
                print('Return operation Cancelled')
            
def show_issuedbooks():
    idf = pd.read_csv('Issuebooks.csv')
    print(idf)
    
def delete_issuedbooks():
    book_name = input('Enter Book Name : ')
    bdf = pd.read_csv('Issuebooks.csv')
    bdf = bdf.drop(bdf[bdf['book_name']==book_name].index)
    bdf.to_csv('Issuebooks.csv',index=False)
    print('Deleted Issued book Successfully')
    print(bdf)
    
def show_charts():
    print('1 -> Books and their Cost')
    print('2 -> Number of Books issued by Members')
    ch =int(input('Enter Your Choice : '))
    if ch==1:
        df = pd.read_csv('Book.csv')
        df = df[['title','cost']]
        df.plot('title','cost',kind = 'bar')
        plt.xlabel('title----->')
        plt.ylabel('cost----->')
        plt.show()
    if ch==2:
        df =pd.read_csv('Issuebooks.csv')
        df = df[['numberofbookissued','m_name']]
        df.plot('m_name','numberofbookissued',kind = 'bar')
        plt.xlabel('Member----->')
        plt.ylabel('Books Issued------>')
        plt.show()
    
def login():
    u_name = input('Enter Username : ')
    pwd = input('Enter Password : ')
    df = pd.read_csv('Users.csv')
    df = df.loc[df['username']==u_name]
    if df.empty:
        print('Invalid Username')
        return False
    else:
        df = df.loc[df['password']==pwd]
        if df.empty:
            print('invalid Password')
            return False
        else:
            print('Username and Password matched Successfully')
            return True
            
def show_menu():
    print('-----------------------------------------------------'              )
    print('             DIGITAL LIBRARY ASSOCIATION             ')
    print('-----------------------------------------------------'              )
    print('1 --> Add new Book')
    print('2 --> Search for a Book')
    print('3 --> Delete a Book')
    print('4 --> Show all Books')
    print('5 --> Add a new Member')
    print('6 --> Search for a Member')
    print('7 --> Delete a Member')
    print('8 --> Show all Members')
    print('9 --> Issue a Book')
    print('10 --> Return a Book')
    print('11 --> Show all issued Books')
    print('12 --> Delete an issued Book')
    print('13 --> To view Charts')
    print('14 --> To exit')
    choice=int(input('Enter your Choice : '))
    return choice
    
#FrontEnd
print('----------WELCOME TO DIGITAL LIBRARY ASSOCIATION-------------')
if login():
    while True:
        ch = show_menu()
        if ch == 1:
            new_entry()
        elif ch == 2:
            search_book()
        elif ch == 3:
            delete_book()
        elif ch == 4:
            show_book()
        elif ch == 5:
            new_member()
        elif ch == 6:
            search_member()
        elif ch == 7:
            delete_member()
        elif ch == 8:
            show_member()
        elif ch == 9:
            issue_book()
        elif ch == 10:
            return_book()
        elif ch == 11:
            show_issuedbooks()
        elif ch == 12:
            delete_issuedbooks()
        elif ch == 13:
            show_charts()
        elif ch == 14:
            break
        else:
            print('Invalid Option Selected')
        
print('Thank You')