import view
import text
import module


def search_contacts():
    word = view.input_data(text.search_word)
    result = module.search(word)
    view.show_contacts(result, text.not_found(word))
    return result


def start():
    while True:
        user_select = view.show_menu(text.main_menu)
        match user_select:
            case 1:
                module.open_file()
                view.print_msg(text.load_successfull)
            case 2:
                module.save_file()
                view.print_msg(text.save_successfull)
            case 3:
                book = module.phone_book
                view.show_contacts(book, text.empty_book)
            case 4:
                new = view.contact_input(text.new_contat)
                module.add_contact(new)
                view.print_msg(text.added_successfull(new[0]))
            case 5:
                search_contacts()
            case 6:
                if search_contacts():
                    uid = view.input_number(text.change_contact)
                    new = view.contact_input(text.rename_contact)
                    name = module.change_contact(uid, new)
                    view.print_msg(text.rename_result(name))
            case 7:
                if search_contacts():
                    uid = view.input_number(text.delete_input)
                    name = module.delete_contact(uid)
                    view.print_msg(text.delete_result(name))
            case 8:
                if module.phone_book != module.original_pb:
                    if view.input_data(text.save_content) == "y":
                        module.save_file()
                        view.print_msg(text.save_successfull)
                view.print_msg(text.good_bay)
                break
