import sqlite3
#? add SELECT methods


class DatabaseHandler:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("VaultLang.db")
        self.cur = self.conn.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON;")

    def get_max_rowid(self, table_name: str) -> int:
        self.cur.execute("SELECT MAX(ROWID) FROM %s;" % (table_name))
        max_rowid = self.cur.fetchone()[0]
        if max_rowid is None:
            return 0
        return max_rowid

    def add_new_lang(self, lang_name: str) -> None:
        lang_id = self.get_max_rowid("languages") + 1
        self.cur.execute("INSERT INTO languages VALUES(%s, '%s')" % (lang_id, lang_name))
        self.conn.commit()

    def add_category(self, category_name: str) -> None:
        category_id = self.get_max_rowid("categories") + 1
        self.cur.execute("INSERT INTO categories VALUES(%s, '%s')" % (category_id, category_name))
        self.conn.commit()

    def add_new_word(self, word_data: list) -> None:
        word_id = self.get_max_rowid("words_storage") + 1
        word_data.insert(0, word_id)

        query = '''
        INSERT INTO words_storage (word_id, native_word, transcription, translation, word_condition, category_id, lang_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''

        self.cur.execute(query, word_data)
        self.conn.commit()

    def add_several_words(self, words_data: list) -> None:
        word_id = self.get_max_rowid("words_storage")
        for position, item in enumerate(words_data):
            word_position = word_id + position + 1
            item.insert(0, word_position)

        query = '''
        INSERT INTO words_storage (word_id, native_word, transcription, translation, word_condition, category_id, lang_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''

        self.cur.executemany(query, words_data)
        self.conn.commit()

    def delete_lang(self, lang_name: str):
        self.cur.execute("DELETE FROM languages WHERE lang_name = '%s'" % (lang_name))
        self.conn.commit()

    def delete_category(self, category_name: str):
        self.cur.execute("DELETE FROM categories WHERE category_name = '%s'" % (category_name))
        self.conn.commit()

    def delete_word(self, native_word):
        self.cur.execute("DELETE FROM words_storage WHERE native_word = %s;" % (native_word))
        self.conn.commit()

    def edit_word(self, word_id, column_name, new_data):
        self.cur.execute("UPDATE words_storage SET '%s' = '%s' WHERE word_id = %s" % (column_name, new_data, word_id))
        self.conn.commit()
