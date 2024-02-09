class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.targets = []

    def add_target(self, target):
        self.targets.append(target)

    def update_target(self, index, new_target):
        if 0 <= index < len(self.targets):
            self.targets[index] = new_target
            print("Hedef güncellendi.")
        else:
            print("Geçersiz hedef no.")

    def delete_target(self, index):
        if 0 <= index < len(self.targets):
            del self.targets[index]
        else:
            print("Geçersiz hedef no.")


class Target:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority


class UserManager:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password):
        if username in self.users:
            print("Bu kullanıcı adı zaten mevcut.")
        else:
            self.users[username] = User(username, password)
            print("Kullanıcı oluşturuldu.")

    def login(self, username, password):
        if username in self.users:
            if self.users[username].password == password:
                print("Hoş geldiniz,", username)
                return self.users[username]
            else:
                print("Geçersiz şifre. Lütfen tekrar deneyin.")
                return None
        else:
            print("Geçersiz kullanıcı adı. Lütfen tekrar deneyin.")
            return None


def main():
    user_manager = UserManager()
    while True:
        print("\n==== Hedef Yönetim Sistemi ====")
        print("1. Kayıt Ol")
        print("2. Giriş Yap")
        print("3. Çıkış")

        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            username = input("Kullanıcı adı: ")
            password = input("Şifre: ")
            user_manager.create_user(username, password)
        elif choice == "2":
            username = input("Kullanıcı adı: ")
            password = input("Şifre: ")
            user = user_manager.login(username, password)
            if user:
                while True:
                    print("\nHedef Yönetimi:")
                    print("1. Hedefleri Görüntüle")
                    print("2. Hedef Ekle")
                    print("3. Hedef Güncelle")
                    print("4. Hedef Sil")
                    print("5. Çıkış")

                    choice = input("Seçiminizi yapın: ")

                    if choice == "1":
                        print("Hedefler:")
                        for i, target in enumerate(user.targets):
                            print(f"{i+1}. {target.description} - Öncelik :{target.priority}")
                    elif choice == "2":
                        description = input("Hedef açıklaması: ")
                        priority = int(input("Öncelik no (1, 2, 3, ...) girin: "))
                        user.add_target(Target(description, priority))
                        print("Hedef eklendi.")
                    elif choice == "3":
                        index = int(input("Güncellenecek hedef no: ")) - 1
                        if 0 <= index < len(user.targets):
                            description = input("Yeni hedef açıklaması: ")
                            priority = int(input("Yeni öncelik no (1, 2, 3, ...) girin: "))
                            user.update_target(index, Target(description, priority))
                            print("Hedef güncellendi.")
                        else:
                            print("Geçersiz hedef no. Lütfen kayıtlı bir hedef numarası girin.")
                    elif choice == "4":
                        index = int(input("Silinecek hedef no: ")) - 1
                        if 0 <= index < len(user.targets):
                            user.delete_target(index)
                        else:
                            print("Geçersiz hedef no. Hedef silmek için öncelikle hedefleri görüntüleyebilirsiniz.")
                    elif choice == "5":
                        break
                    else:
                        print("Geçersiz seçim.")
        elif choice == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()
