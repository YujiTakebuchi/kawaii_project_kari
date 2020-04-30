import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


DISCORD = 'DISCORD'
TWITTER = 'TWITTER'

cred = credentials.Certificate("/Users/s1230218/Downloads/kawaii-project-kari-firebase-adminsdk-eks01-bb61710fdf.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# User登録
def register_user(discordId, twitterId, accountType, name):
    
    doc_ref = db.collection(u'User').document()
    doc_ref.set({
                u'id': doc_ref.id,
                u'discordId': discordId,
                u'twitterId': twitterId,
                u'accountType': accountType,
                u'name': name
                })

# User取得
def get_all_user() :
    return db.collection(u'User').stream()

# User更新

# User削除


# コメントデータの追加
# コメント登録用の関数
def comment_regist(discoId,comment): # discoId:message.author.idでコメント発言者のdiscoIdを確認！
    user_doc = db.collection(u'User').where(u'discoId', u'==', u'{}'.format(discoId)).stream() # discoIdを元に発言者の情報を取得
    
    for doc in user_doc:
        user_id = doc.get('id')
    roommember_doc = db.collection(u'RoomMember').where(u'userId', u'==',user_id).stream()
    for doc in roommember_doc:
        room_id = doc.get('roomId')

    doc_ref = db.collection(u'Comment').document()
    doc_ref.set({
                u'comment': comment,
                u'id': user_id, # 発言者のid
                u'roomId': room_id,
                u'userId': user_id
                })

# コメントデータの削除
## delete_comment:デリート対象のコメント
def delete_comment(comment):
    comment_doc = db.collection(u'Comment').where(u'comment', u'==', u'{}'.format(comment)).stream()
    for doc in comment_doc:
        doc_id = doc.id
        db.collection(u'Comment').document(u'{}'.format(doc_id)).delete()
    print('deleted!')


# コメントデータの取得、表示
# コメントをunityで表示
def comment_display(discoId,comment):
    comment_doc = db.collection(u'Comment').stream()
    
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))

# コメントデータ更新
def comment_edit(before_comment,after_comment):
    comment_doc = db.collection(u'Comment').where(u'comment', u'==', u'{}'.format(before_comment)).stream()
    for doc in comment_doc:
        edit_doc = db.collection(u'Comment').document(u'{}'.format(doc.id))
        edit_doc.update({u'comment': after_comment})


# RoomMember登録
def register_room_member(id, user_id, room_id):
    
    register_user(id, user_id, room_id, False, False)


def register_room_member(user_id, room_id, is_blocked, is_admin):
    
    doc_ref = db.collection(u'RoomMember').document()
    doc_ref.set({
                u'id': doc_ref.id,
                u'userId': user_id,
                u'roomId': room_id,
                u'isBlocked': is_blocked,
                u'isAdmin': is_admin
                })

# RoomMember取得

# RoomMember更新

# RoomMember削除


# 未登録User確認

#def register_unknown_user(discord_id, name) :
#
#    if (not check_is_user_registered(discord_id)) :
#        print(discord_id)
#        register_user(discord_id, '', DISCORD, name)

def register_unknown_user(user) :
    
        print(user.id)
        print(user.name)
        if (not check_is_user_registered(user.id)) :
            print(user.id)
            register_user(user.id, '', DISCORD, user.name)


def register_unknown_users(users) :
    
    for user in users :
        register_unknown_user(user)


def check_is_user_registered(discord_id) :

    for user in get_all_user() :
        if discord_id == user.to_dict().get('discordId') :
            return True

    return False


# テスト用
def test(discoId,comment):
    user_doc = db.collection(u'User').where(u'discoId', u'==', u'{}'.format(discoId)).stream() # discoIdを元に発言者の情報を取得
    
    for doc in user_doc:
        user_id = doc.get('id')
    roommember_doc = db.collection(u'RoomMember').where(u'userId', u'==',user_id).stream()
    for doc in roommember_doc:
        room_id = doc.get('roomId')
    print(user_id)
    print(room_id)
    print(comment)
