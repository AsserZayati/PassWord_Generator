import math
import customtkinter as ctk
import string
import random




def generer():
    N=Input_mdp.get()
    lst=[]
    while True:
        try :
            n=int(N)
            if ((n<4) or (n>12)):
                mdp_label.configure(text="Votre longeur choisit est trop court ou trop long...change le.")
                break 
        except :
            mdp_label.configure(text='Une erreur est survenu, verifiez encore..')
            break
        else:
            lst.append(string.digits)
            lst[0]=lst[0]+string.punctuation
            lst[0]=lst[0]+string.ascii_letters
            MDP_choice=random.choices(lst[0],k=n)
            MDP = "".join(MDP_choice)
            mdp_label.configure(text=f"Voici votre mot de passe : {MDP}")
            btn.configure(text='Generer a nouveau')
            break

        



root=ctk.CTk()
root.geometry('500x390')
root.title("MDP Generateur")
root.resizable(height=False,width=False)
labe_choix=ctk.CTkLabel(root,text='Entrer la longeur de votre mot de passe que vous souhaitez ...',font=("Arial",15))
labe_choix.place(relx=0.5,rely=0.2,anchor=ctk.S)
Input_mdp=ctk.CTkEntry(root,placeholder_text="Entrer la longeur ici ....")
Input_mdp.place(relx=0.5,rely=0.24,anchor=ctk.N)

btn=ctk.CTkButton(master=root,text='Generer MDP',fg_color='blue',height=55,font=('Helvetica',22,'italic'),hover_color='red',command=generer)
btn.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
mdp_label=ctk.CTkLabel(root,text="Votre mot de passe s'affiche Ici ..",font=("Arial",16))
mdp_label.place(relx=0.5,rely=0.7,anchor=ctk.CENTER)

root.mainloop()