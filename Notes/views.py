import random
import re

from django.core.mail import EmailMessage
from django.http import HttpResponse, request
from django.shortcuts import redirect, render

from Notes.models import notes, signup

# Create your views here.


# <-------------------Signup------------------>
def Signup(request):
    email_regEx = re.compile(r"^[a-z][a-zA-Z0-9-_.]+@[a-zA-Z]+\.[a-z]{3,5}+")
    uname_regEx = re.compile(r"^[A-Z][a-zA-Z\s]+")
    pwd_regEx = re.compile(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    )
    if request.method == "POST":
        email = request.POST.get("email")
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        cpwd = request.POST.get("cpwd")
        check_existing_user = signup.objects.filter(email=email)

        if check_existing_user:
            return HttpResponse("User with this email id already exists.")

        elif email and (not email_regEx.search(email)):
            return HttpResponse("Email must start with small case alphabet.")

        elif uname and (not uname_regEx.search(uname)):
            return HttpResponse("Username must start with capital case letter.")

        elif pwd and (not pwd_regEx.search(pwd)):
            return HttpResponse(
                "Minimum 8+ chars, atleast 1 Uppercase, 1 Lowercase, 1 Number, and 1 special Chars."
            )

        elif email == "" or uname == "" or pwd == "" or cpwd == "":
            return HttpResponse("fields can't be left blank.")

        elif (
            (email_regEx.search(email))
            and (uname_regEx.search(uname))
            and pwd == cpwd
            and (pwd_regEx.search(pwd))
            and request.POST.get("otp")
        ):
            otp = request.POST.get("otp")
            if int(otp) == int(request.session["random"]):
                newUser = signup.objects.create(
                    username=uname, email=email, password=pwd, status="inactive"
                )
                newUser.save()
                activeUser = signup.objects.filter(email=email)
                for userStatus in activeUser:
                    userStatus.status = "active"
                    userStatus.save()
                del request.session["email"]
                del request.session["random"]
                return HttpResponse("otp matched")
            else:
                return HttpResponse("Incorrect OTP.")

        elif (
            (email_regEx.search(email))
            and (uname_regEx.search(uname))
            and pwd == cpwd
            and (pwd_regEx.search(pwd))
        ):
            request.session["email"] = email
            return HttpResponse("submit")

        elif pwd != cpwd and (pwd_regEx.search(pwd)):
            return HttpResponse("Password and Confirm Password does not match.")

    return render(request, "SignUp.html")


# <-------------------------Signup-------------------------->


# <-------------------------Send OTP-------------------------->
def SendOtp(request):
    request.session["random"] = random.randint(1000, 9999)
    mail_subject = "Your activation code is " + str(request.session["random"])
    email = EmailMessage("hello", mail_subject, to=[request.session["email"]])
    email.send()
    return HttpResponse("OTP has been sent, check your email id.")


# <-------------------------Send OTP-------------------------->


# <-------------------Login------------------>
def Login(request):
    # del request.session["email1"]
    # del request.session["id"]
    if request.method == "POST":
        if (not request.POST.get("email2")) and (not request.POST.get("password")):
            return HttpResponse("fields can't be left blank.")

        elif request.POST.get("email2") and request.POST.get("password"):
            email2 = request.POST.get("email2")
            password = request.POST.get("password")
            user_data = signup.objects.filter(email=email2)

            for userInfo in user_data:
                if userInfo.email == email2 and userInfo.password == password:
                    request.session["email1"] = email2
                    request.session["id"] = userInfo.id
                    return HttpResponse("login")
                break
            if len(user_data) == 0:
                return HttpResponse("Email and Password did not match.")

    return render(request, "Login.html")


# <-------------------Login------------------>


# <---------------------- otp for resetting password ----------------->
def resetOtp(request):
    request.session["random1"] = random.randint(1000, 9999)
    mail_subject = "Your otp for reset password is " + str(request.session["random1"])
    email = EmailMessage("Hi there", mail_subject, to=[request.session["email3"]])
    email.send()
    return HttpResponse("OTP has been sent, check your mail.")


# <---------------------- otp for resetting password ----------------->


# <-------------------Forgot password page------------------>


def forgotPassword(request):
    reset_pwd_regEx = re.compile(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    )
    if request.method == "POST":
        if request.POST.get("newPassword") and request.POST.get("confirmNewPassword"):
            newPassword = request.POST.get("newPassword")
            confirmNewPassword = request.POST.get("confirmNewPassword")
            if (not request.POST.get("newPassword")) and (
                not request.POST.get("confirmNewPassword")
            ):
                return HttpResponse("Field's can't be left blank.")

            if (
                reset_pwd_regEx.search(newPassword)
                and newPassword != confirmNewPassword
            ):
                return HttpResponse(
                    "New Password and Confirm New Password do not match."
                )

            elif (
                not reset_pwd_regEx.search(newPassword)
            ) and newPassword == confirmNewPassword:
                return HttpResponse(
                    "Minimum 8+ chars, atleast 1 Uppercase, 1 Lowercase, 1 Number, and 1 special Chars."
                )

            elif (
                reset_pwd_regEx.search(newPassword)
                and newPassword == confirmNewPassword
            ):
                newuser = signup.objects.filter(email=request.session["email3"])
                for newUser in newuser:
                    newUser.password = newPassword
                    newUser.save()
                    del request.session["email3"]
                    del request.session["random1"]
                return HttpResponse("next")

        if request.POST.get("resetOtp"):
            resetOTP = request.POST.get("resetOtp")
            if int(resetOTP) == int(request.session["random1"]):
                return HttpResponse("match")
            else:
                return HttpResponse("incorrect OTP")

        if request.POST.get("email"):
            email = request.POST.get("email")
            user = signup.objects.filter(email=email)
            for emailData in user:
                if emailData.email == email:
                    request.session["email3"] = email
                    return HttpResponse("Email found.")
                break
            if len(user) == 0:
                return HttpResponse(
                    "Couldn't find such email, check your email once again."
                )
        if not request.POST.get("email"):
            return HttpResponse("Field can't be left blank.")

    return render(request, "ForgotPassword.html")


# <-------------------Forgot password page------------------>


def Logout(request):
    del request.session["email1"]
    del request.session["id"]
    return HttpResponse("logout")


# <-------------------NotesApp------------------>
def NoteApp(request):
    userNotes = notes.objects.filter(user_id=request.session["id"])
    data = {"userNotes": userNotes}
    if request.method == "POST":
        todoTitle = request.POST.get("noteTitle")
        userID = request.POST.get("userId")
        description = request.POST.get("description")
        if todoTitle and description:
            note = notes.objects.create(
                title=todoTitle, description=description, user_id=userID
            )
            note.save()
            return HttpResponse("note saved.")

    return render(request, "NoteApp.html", data)


# <-------------------NotesApp------------------>


def Delete(request, id):
    note = notes.objects.get(id=id)
    note.delete()
    return redirect("/NoteApp/")


def Demo(request):
    return render(request, "Demo.html")
