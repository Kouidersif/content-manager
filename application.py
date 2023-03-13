import customtkinter as ctk
import requests
import json
import webbrowser


ctk.set_appearance_mode("Dark")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.file_path = None
        # configure window
        self.title("Content Manager")
        self.geometry(f"{1100}x{620}")
        self.h1tag = ctk.CTkLabel(self, text="Share Content from Desktop", font=("Arial", 26))
        self.h1tag.pack(pady=10, padx=10)
        #Create input to get blog title
        self.label = ctk.CTkLabel(self, text="Blog Title")
        self.label.pack(pady=10, padx=10)
        self.string_input_button = ctk.CTkEntry(self, placeholder_text="Tutorial: How to deploy Django Application", width=350)
        self.string_input_button.pack(pady=10, padx=10)
        self.content_preview = ctk.CTkTextbox(self, width=350, height=300)
        self.content_preview.pack()
        self.upload_button = ctk.CTkButton(self, text="Upload Content", command=self.upload_file)
        self.upload_button.pack(pady=10, padx=10)
        self.save_button = ctk.CTkButton(self, text="Save Changes", command=self.send_post_request)
        self.save_button.pack(pady=10, padx=10)

    def open_input_dialog_event(self):
        dialog = self.string_input_button.get()
        return dialog
    def upload_file(self):
        if self.file_path == None:
            get_file = ctk.filedialog.askopenfilename()
            with open(get_file, "r") as file:
                self.file_path = file.read()
                self.content_preview.insert("1.0", text=self.file_path)
        return self.file_path
    def send_post_request(self):
        # call the open_input_dialog_event and upload_file methods to get their return values
        title = self.open_input_dialog_event()
        content = self.upload_file()
        # define the JSON dictionary
        data = {
            "title": str(title),
            "content":str(content),
            "author": int(1),
            "category": int(1)
        }
        headers = {
            "Content-Type": "application/json"
        }
        
        response = requests.post("http://127.0.0.1:8080/api/post/", json=data, headers=headers)
        if response.status_code == 201:
            
            url = "http://127.0.0.1:8080/api/blog/"
            # Reset all inputs
            self.file_path = None
            #Success message + url to the blog api
            self.success_label = ctk.CTkLabel(self, text=f"Post Has been sucessfully shared")
            response_dict = json.loads(response.content)
            self.success_btn = ctk.CTkButton(self, text="View Blog", 
                                            command= lambda : webbrowser.open(url + str(response_dict["id"])) )
            self.success_label.pack()
            self.success_btn.pack()
        # print the response status code and content
        print("Status code:", response.content)






if __name__ == "__main__":
    app = App()
    app.mainloop()