from admin_module import User, Admin

admin = Admin('hadi', 'suhada', 'admin', 'cirebon')
print(admin.describe_user())
admin.privillage.show_privillages()