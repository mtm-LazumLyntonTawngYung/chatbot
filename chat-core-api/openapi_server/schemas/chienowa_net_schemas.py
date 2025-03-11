# ----------------------------------------------------------------
# DO NOT MODIFY MANUALLY without a bug fix.
# You can generate this code by using /scripts/sqlacodegen
# `from sqlalchemy.orm import relationship` will conflict with Colmun name `relationship`
# So you must fix as `from sqlalchemy.orm import relationship as _relationship`
# and replace relationship method to _relationship
# ----------------------------------------------------------------
from sqlalchemy import CHAR, Column, Date, DateTime, Float, ForeignKey, ForeignKeyConstraint, Index, String, TIMESTAMP, Text, Time, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, LONGTEXT, MEDIUMINT, MEDIUMTEXT, TINYINT, TINYTEXT
from sqlalchemy.orm import relationship as _relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class WpBpActivity(Base):
    __tablename__ = 'wp_bp_activity'

    id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20), nullable=False, index=True)
    component = Column(String(75), nullable=False, index=True)
    type = Column(String(75), nullable=False, index=True)
    action = Column(Text, nullable=False)
    content = Column(LONGTEXT, nullable=False)
    primary_link = Column(Text, nullable=False)
    item_id = Column(BIGINT(20), nullable=False, index=True)
    secondary_item_id = Column(BIGINT(20), index=True)
    date_recorded = Column(DateTime, nullable=False, index=True)
    hide_sitewide = Column(TINYINT(1), index=True, server_default=text("'0'"))
    mptt_left = Column(INTEGER(11), nullable=False,
                       index=True, server_default=text("'0'"))
    mptt_right = Column(INTEGER(11), nullable=False,
                        index=True, server_default=text("'0'"))
    is_spam = Column(TINYINT(1), nullable=False,
                     index=True, server_default=text("'0'"))


class WpBpActivityMeta(Base):
    __tablename__ = 'wp_bp_activity_meta'

    id = Column(BIGINT(20), primary_key=True)
    activity_id = Column(BIGINT(20), nullable=False, index=True)
    meta_key = Column(String(255), index=True)
    meta_value = Column(LONGTEXT)


class WpBpNotification(Base):
    __tablename__ = 'wp_bp_notifications'
    __table_args__ = (
        Index('useritem', 'user_id', 'is_new'),
    )

    id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20), nullable=False, index=True)
    item_id = Column(BIGINT(20), nullable=False, index=True)
    secondary_item_id = Column(BIGINT(20), index=True)
    component_name = Column(String(75), nullable=False, index=True)
    component_action = Column(String(75), nullable=False, index=True)
    date_notified = Column(DateTime, nullable=False)
    is_new = Column(TINYINT(1), nullable=False,
                    index=True, server_default=text("'0'"))


class WpBpNotificationsMeta(Base):
    __tablename__ = 'wp_bp_notifications_meta'

    id = Column(BIGINT(20), primary_key=True)
    notification_id = Column(BIGINT(20), nullable=False, index=True)
    meta_key = Column(String(255), index=True)
    meta_value = Column(LONGTEXT)


class WpBpUserBlog(Base):
    __tablename__ = 'wp_bp_user_blogs'

    id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20), nullable=False, index=True)
    blog_id = Column(BIGINT(20), nullable=False, index=True)


class WpBpUserBlogsBlogmeta(Base):
    __tablename__ = 'wp_bp_user_blogs_blogmeta'

    id = Column(BIGINT(20), primary_key=True)
    blog_id = Column(BIGINT(20), nullable=False, index=True)
    meta_key = Column(String(255), index=True)
    meta_value = Column(LONGTEXT)


class WpBpXprofileDatum(Base):
    __tablename__ = 'wp_bp_xprofile_data'

    id = Column(BIGINT(20), primary_key=True)
    field_id = Column(BIGINT(20), nullable=False, index=True)
    user_id = Column(BIGINT(20), nullable=False, index=True)
    value = Column(LONGTEXT, nullable=False)
    last_updated = Column(DateTime, nullable=False)


class WpBpXprofileField(Base):
    __tablename__ = 'wp_bp_xprofile_fields'

    id = Column(BIGINT(20), primary_key=True)
    group_id = Column(BIGINT(20), nullable=False, index=True)
    parent_id = Column(BIGINT(20), nullable=False, index=True)
    type = Column(String(150), nullable=False)
    name = Column(String(150), nullable=False)
    description = Column(LONGTEXT, nullable=False)
    is_required = Column(TINYINT(1), nullable=False,
                         index=True, server_default=text("'0'"))
    is_default_option = Column(
        TINYINT(1), nullable=False, server_default=text("'0'"))
    field_order = Column(BIGINT(20), nullable=False,
                         index=True, server_default=text("'0'"))
    option_order = Column(BIGINT(20), nullable=False,
                          server_default=text("'0'"))
    order_by = Column(String(15), nullable=False, server_default=text("''"))
    can_delete = Column(TINYINT(1), nullable=False,
                        index=True, server_default=text("'1'"))


class WpBpXprofileGroup(Base):
    __tablename__ = 'wp_bp_xprofile_groups'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(150), nullable=False)
    description = Column(MEDIUMTEXT, nullable=False)
    group_order = Column(BIGINT(20), nullable=False,
                         server_default=text("'0'"))
    can_delete = Column(TINYINT(1), nullable=False, index=True)


class WpBpXprofileMeta(Base):
    __tablename__ = 'wp_bp_xprofile_meta'

    id = Column(BIGINT(20), primary_key=True)
    object_id = Column(BIGINT(20), nullable=False, index=True)
    object_type = Column(String(150), nullable=False)
    meta_key = Column(String(255), index=True)
    meta_value = Column(LONGTEXT)


class WpCommentmeta(Base):
    __tablename__ = 'wp_commentmeta'

    meta_id = Column(BIGINT(20), primary_key=True)
    comment_id = Column(BIGINT(20), nullable=False,
                        index=True, server_default=text("'0'"))
    meta_key = Column(String(255, 'utf8mb4_unicode_ci'), index=True)
    meta_value = Column(LONGTEXT)


class WpComment(Base):
    __tablename__ = 'wp_comments'
    __table_args__ = (
        Index('comment_approved_date_gmt',
              'comment_approved', 'comment_date_gmt'),
    )

    comment_ID = Column(BIGINT(20), primary_key=True)
    comment_post_ID = Column(BIGINT(20), nullable=False,
                             index=True, server_default=text("'0'"))
    comment_author = Column(TINYTEXT, nullable=False)
    comment_author_email = Column(String(
        100, 'utf8mb4_unicode_ci'), nullable=False, index=True, server_default=text("''"))
    comment_author_url = Column(
        String(200, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("''"))
    comment_author_IP = Column(
        String(100, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("''"))
    comment_date = Column(DateTime, nullable=False,
                          server_default=text("'0000-00-00 00:00:00'"))
    comment_date_gmt = Column(
        DateTime, nullable=False, index=True, server_default=text("'0000-00-00 00:00:00'"))
    comment_content = Column(
        Text(collation='utf8mb4_unicode_ci'), nullable=False)
    comment_karma = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"))
    comment_approved = Column(
        String(20, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("'1'"))
    comment_agent = Column(String(255, 'utf8mb4_unicode_ci'),
                           nullable=False, server_default=text("''"))
    comment_type = Column(String(20, 'utf8mb4_unicode_ci'),
                          nullable=False, server_default=text("''"))
    comment_parent = Column(BIGINT(20), nullable=False,
                            index=True, server_default=text("'0'"))
    user_id = Column(BIGINT(20), nullable=False, server_default=text("'0'"))


class WpCpdCounter(Base):
    __tablename__ = 'wp_cpd_counter'
    __table_args__ = (
        Index('idx_dateip', 'date', 'ip'),
    )

    id = Column(INTEGER(10), primary_key=True)
    ip = Column(INTEGER(10), nullable=False)
    client = Column(String(500), nullable=False)
    date = Column(Date, nullable=False)
    page = Column(MEDIUMINT(9), nullable=False, index=True)
    country = Column(CHAR(2), nullable=False)
    referer = Column(String(500), nullable=False)


class WpGsAdminAttributeGroup(Base):
    __tablename__ = 'wp_gs_admin_attribute_group'
    __table_args__ = {
        'comment': '任意の属性グループを管理するテーブル\\r\\n複数の属性情報を１つのグループとして扱うことができる'}

    id = Column(BIGINT(20), primary_key=True, comment='属性グループID')
    group_name = Column(String(256), nullable=False, comment='属性グループ名')


class WpGsAdminCareinfoParentCluster(Base):
    __tablename__ = 'wp_gs_admin_careinfo_parent_cluster'
    __table_args__ = (
        Index('wp_gs_admin_careinfo_parent_cluster_idx', 'cluster_order', 'id'),
        {'comment': 'ケア体験の「おきたこと」でグルーピングした結果のGP・BP集計用親クラスタ。おきたことの代表文、カテゴリを格納する。'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='「おきたこと」グループ識別子')
    happen_represent = Column(Text, nullable=False, comment='「おきたこと」代表文')
    happen_core = Column(Text, nullable=False, comment='「おたこと」コア文')
    happen_draft = Column(Text, nullable=False, comment='「おきたこと」代表文下書き')
    category = Column(Text, nullable=False, comment='カテゴリ')
    other_category = Column(Text, nullable=False, comment='他にも考えられるカテゴリ')
    good_practice_num = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='うまくいった件数')
    bad_practice_num = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='うまくいかなかった件数')
    cluster_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='クラスタ状態(0:状態なし,1:新規,2:代表文選出,3:既存)')
    represent_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='代表文選出状態(0:未選出,1:選出済,2:確認済,3:承認済)')
    represent_check_result = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='代表文判定結果(0:未選択,1:OK,2:NG)')
    rule_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='ルール更新状態(0：状態なし、1：要更新)')
    cluster_order = Column(INTEGER(11), nullable=False,
                           server_default=text("'10'"), comment='クラスタの並び順')


class WpGsAdminCombineParentCluster(Base):
    __tablename__ = 'wp_gs_admin_combine_parent_cluster'
    __table_args__ = (
        Index('wp_gs_admin_combine_parent_cluster_idx',
              'group_task_group_id', 'parent_cluster_id'),
        {'comment': '結合・分割対象「おきたこと」グループ情報'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='結合・分割対象「おきたこと」グループ識別子')
    group_task_group_id = Column(
        BIGINT(20), nullable=False, comment='グループタスクグループID')
    parent_cluster_id = Column(BIGINT(20), nullable=False, server_default=text(
        "'0'"), comment='「おきたこと」グループ識別子')
    happen_represent = Column(Text, comment='「おきたこと」代表文')


class WpGsAdminDeleteHistory(Base):
    __tablename__ = 'wp_gs_admin_delete_history'
    __table_args__ = (
        Index('wp_gs_admin_delete_history_idx', 'delete_history_type',
              'history_target_id', 'delete_date'),
        {'comment': '管理者サイトにおける削除履歴を格納するテーブル。'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='履歴ID')
    delete_history_type = Column(INTEGER(11), nullable=False, comment='削除履歴種別')
    history_target_id = Column(BIGINT(20), nullable=False, comment='履歴対象ID')
    history_target_value = Column(Text, nullable=False, comment='履歴対象値')
    delete_date = Column(TIMESTAMP, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='削除日時')


class WpGsAdminGpbpResult(Base):
    __tablename__ = 'wp_gs_admin_gpbp_result'
    __table_args__ = {'comment': 'GP・BP集計結果を管理するテーブル。GP・BP集計結果の選定条件を格納する。'}

    id = Column(BIGINT(20), primary_key=True, comment='GPBP集計結果ID')
    download_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='ダウンロード状態(0：ダウンロード不可、1：集計結果ダウンロード可能、2：集計結果・フロアマップダウンロード可能)')
    result_name = Column(Text, nullable=False, comment='GPBP集計結果の名前')
    start_date = Column(DateTime, nullable=False, comment='集計期間の開始日')
    end_date = Column(DateTime, nullable=False, comment='集計期間の終了日')
    enable_num = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='集計の対象とするのに必要な最少ケア体験数')
    enable_gp_num = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='GPとするのに必要な最少ケア体験数')
    enable_bp_num = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='BPとするのに必要な最少ケア体験数')
    enable_vote = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='集計対象とするのに必要な最少投票数')
    enable_gp_vote = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='GPとするのに必要な最少投票数')
    enable_bp_vote = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='GPとするのに必要な最少投票数')
    enable_gp_rate = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='GPとするのに必要な最低奏功確率(%)')
    enable_bp_rate = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='BPとするのに必要な最高奏功確率(%)')
    selection_gp_num = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='選定するGP数')
    selection_bp_num = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='選定するBP数')


class WpGsAdminGroup(Base):
    __tablename__ = 'wp_gs_admin_group'

    group_id = Column(BIGINT(20), primary_key=True, comment='グループID')
    group_type = Column(INTEGER(11), nullable=False,
                        index=True, comment='グループ種別')
    group_role_name = Column(Text, nullable=False, comment='グループ権限名')
    group_name = Column(Text, comment='グループ名')


class WpGsAdminGroupTaskGroup(Base):
    __tablename__ = 'wp_gs_admin_group_task_group'
    __table_args__ = {'comment': 'グループタスクグループ'}

    group_task_group_id = Column(
        BIGINT(20), primary_key=True, comment='グループタスクグループID')
    task_group_type = Column(INTEGER(11), nullable=False, comment='タスクグループ種別')
    task_group_status = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='タスクグループ状態')
    task_start_date = Column(DateTime, comment='タスク開始日時')
    task_end_date = Column(DateTime, comment='タスク終了日時')
    target_id = Column(INTEGER(11), server_default=text(
        "'0'"), comment='グループタスクの対象となる識別子')


class WpGsAdminMiningCareinfo(Base):
    __tablename__ = 'wp_gs_admin_mining_careinfo'
    __table_args__ = (
        Index('wp_gs_admin_mining_careinfo_idx', 'parent_cluster_id',
              'child_cluster_id', 'cluster_order', 'id'),
        {'comment': 'テキストマイニング用にデータを加工したケア体験。\\r\\nGP・BP集計表示に必要なデータを格納する。\\r\\nグルーピングの結果、クラスタに所属しない場合は、親クラスタID、子クラスタIDのそれぞれに0を設定する。'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='マイニング用ケア体験ID')
    parent_cluster_id = Column(BIGINT(20), nullable=False, server_default=text(
        "'0'"), comment='「おきたこと」グループ識別子')
    child_cluster_id = Column(BIGINT(20), nullable=False, server_default=text(
        "'0'"), comment='「対応方法」グループ識別子')
    src_post_id = Column(BIGINT(20), nullable=False, comment='参照元ケア体験の投稿ID')
    src_post_date = Column(DateTime, nullable=False,
                           index=True, comment='参照元ケア体験の投稿日')
    happen = Column(Text, nullable=False, comment='「おきたこと」原文')
    happen_parse = Column(Text, nullable=False, comment='「おきたこと」分解文')
    cope = Column(Text, nullable=False, comment='「対応方法」原文')
    cope_parse = Column(Text, nullable=False, comment='「対応方法」分解文')
    category = Column(Text, nullable=False, comment='カテゴリ')
    category_etc = Column(Text, nullable=False, comment='カテゴリのその他テキスト')
    other_category = Column(Text, nullable=False, comment='他にも考えられるカテゴリ')
    other_category_etc = Column(
        Text, nullable=False, comment='他にも考えられるカテゴリのその他テキスト')
    keyword = Column(Text, nullable=False, comment='キーワード')
    good_practice_num = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='うまくいった件数')
    bad_practice_num = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='うまくいかなかった件数')
    result = Column(Text, nullable=False, comment='うまくいった／うまくいかなかった')
    reason = Column(Text, nullable=False, comment='うまくいった／うまくいかなかった理由')
    happen_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='おきたこと更新状態(0:未更新、1:更新済み)')
    happen_check_result = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='おきたこと判定結果(0:未選択,1:OK,2:NG)')
    happen_independent = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='おきたこと独立状態(0：独立していない、1：独立している、2：除外)')
    cope_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='対応方法更新状態(0:未更新、1:更新済み)')
    cope_check_result = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='対応方法判定結果(0:未選択,1:OK,2:NG)')
    cope_independent = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='対応方法独立状態(0：独立していない、1：独立している、2：除外)')
    result_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='集計結果承認状態(0:未承認、1:承認済み)')
    cluster_order = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='クラスタの並び順')


class WpGsAdminUserDictionary(Base):
    __tablename__ = 'wp_gs_admin_user_dictionary'
    __table_args__ = (
        Index('wp_gs_admin_user_dictionary_idx', 'user_dic_type', 'id'),
        {'comment': 'ユーザ辞書'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='ユーザ辞書ID')
    user_dic_type = Column(INTEGER(11), nullable=False,
                           comment='ユーザ辞書種別(1：おきたこと、2：対応方法)')
    entry = Column(String(128), nullable=False, comment='表層形')
    left_id = Column(INTEGER(11), nullable=False,
                     server_default=text("'0'"), comment='左文脈ID')
    right_id = Column(INTEGER(11), nullable=False,
                      server_default=text("'0'"), comment='右文脈ID')
    cost = Column(INTEGER(11), nullable=False,
                  server_default=text("'0'"), comment='コスト')
    part = Column(String(64), nullable=False, comment='品詞')
    part_sub_1 = Column(String(64), nullable=False,
                        server_default=text("'*'"), comment='品詞細分類1')
    part_sub_2 = Column(String(64), nullable=False,
                        server_default=text("'*'"), comment='品詞細分類2')
    part_sub_3 = Column(String(64), nullable=False,
                        server_default=text("'*'"), comment='品詞細分類3')
    ctype = Column(String(64), nullable=False,
                   server_default=text("'*'"), comment='活用型')
    cform = Column(String(64), nullable=False,
                   server_default=text("'*'"), comment='活用形')
    original = Column(String(128), nullable=False, comment='原形')
    reading = Column(String(256), nullable=False, comment='読み')
    pronunciation = Column(String(256), nullable=False, comment='発音')


class WpGsBpsdMeta(Base):
    __tablename__ = 'wp_gs_bpsd_meta'
    __table_args__ = (
        Index('search_wp_gs_bpsd_meta_post_id_idx', 'wp_posts_ID', 'id'),
        {'comment': 'おきたことの各属性情報を格納する。'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='おきたことID')
    wp_posts_ID = Column(BIGINT(20), nullable=False, comment='おきたことの投稿ID')
    category = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='ケア情報のカテゴリ(カテゴリID)')
    category_etc = Column(Text, nullable=False, comment='ケア情報のカテゴリのその他テキスト')
    happen = Column(LONGTEXT, nullable=False, comment='おきたこと')


class WpGsBpsdSupportManage(Base):
    __tablename__ = 'wp_gs_bpsd_support_manage'
    __table_args__ = {'comment': '認知症対応方法発見チャート(管理部)'}

    id = Column(BIGINT(20), primary_key=True, comment='チャート管理番号')
    category = Column(Text, nullable=False, comment='カテゴリ')
    happen_represent = Column(Text, nullable=False, comment='「おきたこと」代表文')
    status = Column(INTEGER(11), nullable=False, index=True, server_default=text(
        "'0'"), comment='状態(1：作成中、11：確認待ち、21：承認待ち、99：却下、100：非公開、200：公開)')
    start_node_no = Column(BIGINT(20), nullable=False,
                           server_default=text("'0'"), comment='開始ノード番号')


class WpGsCarerInfo(Base):
    __tablename__ = 'wp_gs_carer_info'
    __table_args__ = (
        Index('type_user_id', 'wp_users_ID', 'id'),
        {'comment': '利用者情報'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='介護者ID')
    wp_users_ID = Column(BIGINT(20), nullable=False, comment='利用者ID')
    carer_status = Column(String(20), nullable=False, comment='利用者情報の公開状態')
    src_carer_id = Column(BIGINT(20), comment='下書き元の利用者情報ID')
    update_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='更新日')
    user_type = Column(INTEGER(11), nullable=False,
                       server_default=text("'0'"), comment='利用者区分')
    nick_name = Column(Text, nullable=False, comment='ニックネーム')
    gender = Column(INTEGER(11), nullable=False,
                    server_default=text("'0'"), comment='性別')
    birthday_era = Column(INTEGER(11), nullable=False,
                          server_default=text("'0'"), comment='生まれた年[年号]')
    birthday = Column(DateTime, nullable=False, comment='生まれた年')
    educational_background = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='教育歴：最終学歴')
    educational_background_etc = Column(
        Text, nullable=False, comment='教育歴：最終学歴のその他テキスト')
    educational_duration = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='教育歴：教育年数')
    address_code = Column(Text, nullable=False, comment='住所の郵便番号(最初の3桁)')
    address_prefecture = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='住所の都道府県名')
    job = Column(INTEGER(11), nullable=False,
                 server_default=text("'0'"), comment='職業')
    job_etc = Column(Text, nullable=False, comment='職業のその他テキスト')
    care_duration = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='介護・医療業務歴(年)')
    care_capacity = Column(Text, nullable=False, comment='介護・医療に関する資格(複数選択)')
    care_capacity_etc = Column(
        Text, nullable=False, comment='介護・医療に関する資格のその他テキスト')
    facility_style = Column(INTEGER(11), nullable=False,
                            server_default=text("'0'"), comment='業務施設の様式')
    facility_style_etc = Column(
        Text, nullable=False, comment='業務施設の様式のその他テキスト')
    facility_style_care = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='介護系業務')
    facility_style_care_etc = Column(
        Text, nullable=False, comment='介護系業務のその他テキスト')
    facility_style_medical = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='医療系業務')
    facility_style_medical_etc = Column(
        Text, nullable=False, comment='医療系業務のその他テキスト')
    facility_style_home = Column(
        Text, nullable=False, comment='介護・医療系業務(在宅サービス・外来診療)(複数選択)')
    facility_style_home_etc = Column(
        Text, nullable=False, comment='介護・医療系業務(在宅サービス・外来診療)のその他テキスト')
    facility_style_admission = Column(
        Text, nullable=False, comment='介護・医療系業務(入所サービス・入院診療)(複数選択)')
    facility_style_admission_etc = Column(
        Text, nullable=False, comment='介護・医療系業務(入所サービス・入院診療)のその他テキスト')
    good_care = Column(Text, comment='得意な介護(介護業務従事者)')
    agree_terms = Column(TINYINT(1), nullable=False,
                         server_default=text("'0'"))
    agree_terms_date = Column(DateTime)


class WpGsFloormapType(Base):
    __tablename__ = 'wp_gs_floormap_type'
    __table_args__ = {'comment': 'フロアマップ種別情報'}

    id = Column(BIGINT(20), primary_key=True, comment='フロアマップ種別ID')
    meta_type = Column(INTEGER(11), nullable=False,
                       comment='属性タイプ(1：フロアマップ、2：タイムライン)')
    meta_group = Column(INTEGER(11), nullable=False, comment='属性グループ')
    slug = Column(Text, nullable=False, comment='フロアマップ種別のスラッグ')
    name = Column(Text, nullable=False, comment='フロアマップ種別の名称')
    type_order = Column(INTEGER(11), nullable=False,
                        server_default=text("'100'"), comment='フロアマップ種別の並び順')
    popup_position = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='ポップアップ出現位置(1:左上、2:右上)')


class WpGsGpbpSummaryBpsd(Base):
    __tablename__ = 'wp_gs_gpbp_summary_bpsd'

    id = Column(INTEGER(11), primary_key=True)
    summary_manage_id = Column(INTEGER(11))
    gpbp_result_meta_id = Column(INTEGER(11))
    parent_cluster_id = Column(BIGINT(11))
    category = Column(Text, nullable=False)
    happen = Column(Text, nullable=False)
    cope = Column(Text, nullable=False)
    gpreason = Column(Text, nullable=False)
    bpreason = Column(Text, nullable=False)
    flag = Column(INTEGER(11), nullable=False)
    recommend_flag = Column(INTEGER(11), nullable=False)
    visible = Column(INTEGER(11), nullable=False)
    belong_post_id = Column(INTEGER(11))
    happen_person = Column(INTEGER(11))
    success_judge = Column(INTEGER(11))
    gender = Column(INTEGER(11))
    cause_disease = Column(Text)
    nursing_level = Column(INTEGER(11))


class WpGsGpbpSummaryManage(Base):
    __tablename__ = 'wp_gs_gpbp_summary_manage'
    __table_args__ = (
        Index('wp_gs_gpbp_summary_manage_idx',
              'summary_type', 'summary_status'),
    )

    id = Column(BIGINT(20), primary_key=True, comment='GPBP集計結果公開管理ID')
    summary_type = Column(INTEGER(11), nullable=False,
                          comment='集計結果種別(1:GPBP集計結果、2:GPBP集計結果(フロアマップ))')
    summary_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='集計結果状態(0:未公開、1:公開)')
    upload_user = Column(BIGINT(20), nullable=False,
                         comment='アップロードしたユーザの利用者ID')
    upload_description = Column(
        String(512), nullable=False, comment='アップロードした集計結果の説明')
    upload_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='アップロード日時')


class WpGsMetaOptionValue(Base):
    __tablename__ = 'wp_gs_meta_option_values'
    __table_args__ = (
        Index('sorted_wp_gs_meta_option_values_idx',
              'option_group', 'position', 'id'),
    )

    id = Column(BIGINT(20), primary_key=True)
    option_group = Column(BIGINT(20), nullable=False,
                          server_default=text("'0'"), comment='選択肢グループ')
    option_value = Column(INTEGER(11), nullable=False, comment='選択肢の値')
    option_label = Column(Text, comment='値の表示名')
    effect_class = Column(String(128), comment='選択肢にクラス名を付与してcssで制御するための設定値')
    extend_enable = Column(INTEGER(1), nullable=False, server_default=text(
        "'0'"), comment='拡張テキストフィールドの使用有無(その他の入力項目)')
    extend_format = Column(
        Text, comment='拡張テキストフィールドの表示形式の指定をする(通常は%inpu_value%で入力項目を表示できる)')
    position = Column(INTEGER(11), nullable=False, server_default=text(
        "'100'"), comment='選択肢の表示順を設定する(ソート用)')


class WpGsMetaType(Base):
    __tablename__ = 'wp_gs_meta_type'

    id = Column(BIGINT(20), primary_key=True)
    type_name = Column(String(20), nullable=False, comment='情報種別名')
    discription = Column(Text, comment='情報種別の説明')


class WpGsNextUserId(Base):
    __tablename__ = 'wp_gs_next_user_id'

    id = Column(BIGINT(20), primary_key=True)
    next_id = Column(BIGINT(20), nullable=False)


class WpLink(Base):
    __tablename__ = 'wp_links'

    link_id = Column(BIGINT(20), primary_key=True)
    link_url = Column(String(255, 'utf8mb4_unicode_ci'),
                      nullable=False, server_default=text("''"))
    link_name = Column(String(255, 'utf8mb4_unicode_ci'),
                       nullable=False, server_default=text("''"))
    link_image = Column(String(255, 'utf8mb4_unicode_ci'),
                        nullable=False, server_default=text("''"))
    link_target = Column(String(25, 'utf8mb4_unicode_ci'),
                         nullable=False, server_default=text("''"))
    link_description = Column(
        String(255, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("''"))
    link_visible = Column(String(20, 'utf8mb4_unicode_ci'),
                          nullable=False, index=True, server_default=text("'Y'"))
    link_owner = Column(BIGINT(20), nullable=False, server_default=text("'1'"))
    link_rating = Column(INTEGER(11), nullable=False,
                         server_default=text("'0'"))
    link_updated = Column(DateTime, nullable=False,
                          server_default=text("'0000-00-00 00:00:00'"))
    link_rel = Column(String(255, 'utf8mb4_unicode_ci'),
                      nullable=False, server_default=text("''"))
    link_notes = Column(MEDIUMTEXT, nullable=False)
    link_rss = Column(String(255, 'utf8mb4_unicode_ci'),
                      nullable=False, server_default=text("''"))


class WpOption(Base):
    __tablename__ = 'wp_options'

    option_id = Column(BIGINT(20), primary_key=True)
    option_name = Column(String(191, 'utf8mb4_unicode_ci'), unique=True)
    option_value = Column(LONGTEXT, nullable=False)
    autoload = Column(String(20, 'utf8mb4_unicode_ci'),
                      nullable=False, server_default=text("'yes'"))


class WpPostmeta(Base):
    __tablename__ = 'wp_postmeta'

    meta_id = Column(BIGINT(20), primary_key=True)
    post_id = Column(BIGINT(20), nullable=False,
                     index=True, server_default=text("'0'"))
    meta_key = Column(String(255, 'utf8mb4_unicode_ci'), index=True)
    meta_value = Column(LONGTEXT)


class WpPost(Base):
    __tablename__ = 'wp_posts'
    __table_args__ = (
        Index('type_status_date', 'post_type',
              'post_status', 'post_date', 'ID'),
    )

    ID = Column(BIGINT(20), primary_key=True)
    post_author = Column(BIGINT(20), nullable=False,
                         index=True, server_default=text("'0'"))
    post_date = Column(DateTime, nullable=False,
                       server_default=text("'0000-00-00 00:00:00'"))
    post_date_gmt = Column(DateTime, nullable=False,
                           server_default=text("'0000-00-00 00:00:00'"))
    post_content = Column(LONGTEXT, nullable=False)
    post_title = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    post_excerpt = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    post_status = Column(String(20, 'utf8mb4_unicode_ci'),
                         nullable=False, server_default=text("'publish'"))
    comment_status = Column(String(20, 'utf8mb4_unicode_ci'),
                            nullable=False, server_default=text("'open'"))
    ping_status = Column(String(20, 'utf8mb4_unicode_ci'),
                         nullable=False, server_default=text("'open'"))
    post_password = Column(String(255, 'utf8mb4_unicode_ci'),
                           nullable=False, server_default=text("''"))
    post_name = Column(String(200, 'utf8mb4_unicode_ci'),
                       nullable=False, index=True, server_default=text("''"))
    to_ping = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    pinged = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    post_modified = Column(DateTime, nullable=False,
                           server_default=text("'0000-00-00 00:00:00'"))
    post_modified_gmt = Column(
        DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    post_content_filtered = Column(LONGTEXT, nullable=False)
    post_parent = Column(BIGINT(20), nullable=False,
                         index=True, server_default=text("'0'"))
    guid = Column(String(255, 'utf8mb4_unicode_ci'),
                  nullable=False, server_default=text("''"))
    menu_order = Column(INTEGER(11), nullable=False,
                        server_default=text("'0'"))
    post_type = Column(String(20, 'utf8mb4_unicode_ci'),
                       nullable=False, server_default=text("'post'"))
    post_mime_type = Column(String(100, 'utf8mb4_unicode_ci'),
                            nullable=False, server_default=text("''"))
    comment_count = Column(BIGINT(20), nullable=False,
                           server_default=text("'0'"))


class WpSignup(Base):
    __tablename__ = 'wp_signups'
    __table_args__ = (
        Index('user_login_email', 'user_login', 'user_email'),
        Index('domain_path', 'domain', 'path')
    )

    signup_id = Column(BIGINT(20), primary_key=True)
    domain = Column(String(200), nullable=False, server_default=text("''"))
    path = Column(String(100), nullable=False, server_default=text("''"))
    title = Column(LONGTEXT, nullable=False)
    user_login = Column(String(60), nullable=False, server_default=text("''"))
    user_email = Column(String(100), nullable=False,
                        index=True, server_default=text("''"))
    registered = Column(DateTime, nullable=False,
                        server_default=text("'0000-00-00 00:00:00'"))
    activated = Column(DateTime, nullable=False,
                       server_default=text("'0000-00-00 00:00:00'"))
    active = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    activation_key = Column(String(50), nullable=False,
                            index=True, server_default=text("''"))
    meta = Column(LONGTEXT)


class WpSmSession(Base):
    __tablename__ = 'wp_sm_sessions'

    session_key = Column(CHAR(32, 'utf8mb4_unicode_520_ci'), primary_key=True)
    session_value = Column(LONGTEXT, nullable=False)
    session_expiry = Column(BIGINT(20), nullable=False)


class WpSubscribe2(Base):
    __tablename__ = 'wp_subscribe2'

    id = Column(INTEGER(11), primary_key=True)
    email = Column(String(64), nullable=False, server_default=text("''"))
    active = Column(TINYINT(1), server_default=text("'0'"))
    date = Column(Date, nullable=False, server_default=text("'2015-11-02'"))
    time = Column(Time, nullable=False, server_default=text("'00:00:00'"))
    ip = Column(CHAR(64), nullable=False, server_default=text("'admin'"))
    conf_date = Column(Date)
    conf_time = Column(Time)
    conf_ip = Column(CHAR(64))


class WpTermRelationship(Base):
    __tablename__ = 'wp_term_relationships'

    object_id = Column(BIGINT(20), primary_key=True,
                       nullable=False, server_default=text("'0'"))
    term_taxonomy_id = Column(BIGINT(
        20), primary_key=True, nullable=False, index=True, server_default=text("'0'"))
    term_order = Column(INTEGER(11), nullable=False,
                        server_default=text("'0'"))


class WpTermTaxonomy(Base):
    __tablename__ = 'wp_term_taxonomy'
    __table_args__ = (
        Index('term_id_taxonomy', 'term_id', 'taxonomy', unique=True),
    )

    term_taxonomy_id = Column(BIGINT(20), primary_key=True)
    term_id = Column(BIGINT(20), nullable=False, server_default=text("'0'"))
    taxonomy = Column(String(32, 'utf8mb4_unicode_ci'),
                      nullable=False, index=True, server_default=text("''"))
    description = Column(LONGTEXT, nullable=False)
    parent = Column(BIGINT(20), nullable=False, server_default=text("'0'"))
    count = Column(BIGINT(20), nullable=False, server_default=text("'0'"))


class WpTermmeta(Base):
    __tablename__ = 'wp_termmeta'

    meta_id = Column(BIGINT(20), primary_key=True)
    term_id = Column(BIGINT(20), nullable=False,
                     index=True, server_default=text("'0'"))
    meta_key = Column(String(255, 'utf8mb4_unicode_520_ci'), index=True)
    meta_value = Column(LONGTEXT)


class WpTerm(Base):
    __tablename__ = 'wp_terms'

    term_id = Column(BIGINT(20), primary_key=True)
    name = Column(String(200, 'utf8mb4_unicode_ci'),
                  nullable=False, index=True, server_default=text("''"))
    slug = Column(String(200, 'utf8mb4_unicode_ci'),
                  nullable=False, index=True, server_default=text("''"))
    term_group = Column(BIGINT(10), nullable=False, server_default=text("'0'"))
    term_order = Column(INTEGER(4), server_default=text("'0'"))


class WpUsermeta(Base):
    __tablename__ = 'wp_usermeta'

    umeta_id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20), nullable=False,
                     index=True, server_default=text("'0'"))
    meta_key = Column(String(255, 'utf8mb4_unicode_ci'), index=True)
    meta_value = Column(LONGTEXT)


class WpUser(Base):
    __tablename__ = 'wp_users'

    ID = Column(BIGINT(20), primary_key=True)
    user_login = Column(String(60, 'utf8mb4_unicode_ci'),
                        nullable=False, index=True, server_default=text("''"))
    user_pass = Column(String(255, 'utf8mb4_unicode_ci'),
                       nullable=False, server_default=text("''"))
    user_nicename = Column(String(50, 'utf8mb4_unicode_ci'),
                           nullable=False, index=True, server_default=text("''"))
    user_email = Column(String(100, 'utf8mb4_unicode_ci'),
                        nullable=False, index=True, server_default=text("''"))
    user_url = Column(String(100, 'utf8mb4_unicode_ci'),
                      nullable=False, server_default=text("''"))
    user_registered = Column(DateTime, nullable=False,
                             server_default=text("'0000-00-00 00:00:00'"))
    user_activation_key = Column(
        String(255, 'utf8mb4_unicode_ci'), nullable=False, server_default=text("''"))
    user_status = Column(INTEGER(11), nullable=False,
                         server_default=text("'0'"))
    display_name = Column(String(250, 'utf8mb4_unicode_ci'),
                          nullable=False, server_default=text("''"))


class WpWpmmSubscriber(Base):
    __tablename__ = 'wp_wpmm_subscribers'

    id_subscriber = Column(BIGINT(20), primary_key=True)
    email = Column(String(50), nullable=False)
    insert_date = Column(DateTime, nullable=False)


class WpGsAdminAttributeGroupValue(Base):
    __tablename__ = 'wp_gs_admin_attribute_group_value'
    __table_args__ = (
        Index('wp_gs_admin_attribute_group_value_idx',
              'attribute_group_id', 'group_value'),
        {'comment': '属性グループの属性値を格納するテーブル'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='属性グループ値ID')
    attribute_group_id = Column(ForeignKey(
        'wp_gs_admin_attribute_group.id'), nullable=False, comment='属性グループID')
    group_value = Column(String(256), nullable=False, comment='属性値')
    table_name = Column(String(128), nullable=False, comment='テーブル名')
    column_name = Column(String(128), nullable=False, comment='カラム名')
    search_type = Column(INTEGER(11), nullable=False,
                         server_default=text("'0'"), comment='検索種別')
    search_value = Column(Text, nullable=False, comment='検索条件の値')
    output_flag = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='出力フラグ(0:出力しない、1:出力する)')
    order_num = Column(INTEGER(11), nullable=False, index=True,
                       server_default=text("'100'"), comment='並び順')

    attribute_group = _relationship('WpGsAdminAttributeGroup')


class WpGsAdminCareinfoChildCluster(Base):
    __tablename__ = 'wp_gs_admin_careinfo_child_cluster'
    __table_args__ = (
        Index('wp_gs_admin_careinfo_child_cluster_idx',
              'parent_cluster_id', 'cluster_order', 'id'),
        {'comment': 'ケア体験の「対応方法」でグルーピングした結果のGP・BP集計用子クラスタ。\\r\\n対応方法、うまくいった理由、うまくいかなか'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='「対応方法」グループ識別子')
    parent_cluster_id = Column(ForeignKey(
        'wp_gs_admin_careinfo_parent_cluster.id'), nullable=False, comment='「おきたこと」グループ識別子')
    happen_core = Column(Text, nullable=False, comment='「おきたこと」コア文')
    cope_represent = Column(Text, nullable=False, comment='「対応方法」代表文')
    cope_core = Column(Text, nullable=False, comment='「対応方法」コア文')
    cope_draft = Column(Text, nullable=False, comment='「対応方法」代表文下書き')
    reason_gp = Column(Text, comment='承認されたうまくいった理由')
    reason_bp = Column(Text, comment='承認されたうまくいかなかった理由')
    floormap_types = Column(Text, comment='承認されたフロアマップ種別IDのリスト')
    good_practice_num = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='うまくいった件数')
    bad_practice_num = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='うまくいかなかった件数')
    recommend_flag = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='お勧めフラグ(0：通常、1：お勧め、2：お勧めでない)')
    cluster_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='クラスタ状態(0:状態なし,1:新規,2:代表文選出,3:既存)')
    represent_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='代表文選出状態(0:未選出,1:選出済,2:確認済,3:承認済)')
    represent_check_result = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='代表文判定結果(0:未選択,1:OK,2:NG)')
    cluster_order = Column(INTEGER(11), nullable=False,
                           server_default=text("'10'"), comment='クラスタの並び順')

    parent_cluster = _relationship('WpGsAdminCareinfoParentCluster')


class WpGsAdminCareinfoParentClusterRule(Base):
    __tablename__ = 'wp_gs_admin_careinfo_parent_cluster_rules'
    __table_args__ = {'comment': 'ケア体験親クラスタ(おきたこと)のルール'}

    parent_cluster_id = Column(ForeignKey('wp_gs_admin_careinfo_parent_cluster.id', ondelete='CASCADE',
                               onupdate='CASCADE'), primary_key=True, nullable=False, comment='「おきたこと」グループ識別子')
    row = Column(INTEGER(11), primary_key=True, nullable=False, comment='行番号')
    value = Column(Text, nullable=False, comment='要素')
    importance = Column(INTEGER(11), nullable=False,
                        server_default=text("'0'"), comment='重要度')

    parent_cluster = _relationship('WpGsAdminCareinfoParentCluster')


class WpGsAdminCombineChildCluster(Base):
    __tablename__ = 'wp_gs_admin_combine_child_cluster'
    __table_args__ = (
        Index('wp_gs_admin_combine_child_cluster_idx', 'group_task_group_id',
              'combine_parent_cluster_id', 'child_cluster_id'),
        {'comment': '結合・分割対象「対応方法」グループ情報'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='結合・分割対象「対応方法」グループ識別子')
    group_task_group_id = Column(
        BIGINT(20), nullable=False, comment='グループタスクグループID')
    combine_parent_cluster_id = Column(ForeignKey('wp_gs_admin_combine_parent_cluster.id', ondelete='CASCADE',
                                       onupdate='CASCADE'), nullable=False, index=True, comment='結合・分割対象「おきたこと」グループ識別子')
    child_cluster_id = Column(BIGINT(20), nullable=False, server_default=text(
        "'0'"), comment='「対応方法」グループ識別子')
    cope_represent = Column(Text, comment='「対応方法」代表文')
    recommend_flag = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='お勧めフラグ(0：通常、1：お勧め、2：お勧めでない)')

    combine_parent_cluster = _relationship('WpGsAdminCombineParentCluster')


class WpGsAdminGpbpCombineGroupOperation(Base):
    __tablename__ = 'wp_gs_admin_gpbp_combine_group_operation'
    __table_args__ = (
        Index('wp_gs_admin_gpbp_combine_group_operation_combine_type_idx',
              'group_task_group_id', 'combine_type', 'id'),
        Index('wp_gs_admin_gpbp_combine_group_operation_idx',
              'group_task_group_id', 'id'),
        {'comment': 'ケア体験グループ結合・分割操作'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='ケア体験グループ結合・分割ID')
    group_task_group_id = Column(ForeignKey('wp_gs_admin_group_task_group.group_task_group_id',
                                 ondelete='CASCADE', onupdate='CASCADE'), nullable=False, comment='グループタスクグループID')
    operation_date = Column(DateTime, nullable=False, comment='操作日時')
    combine_type = Column(INTEGER(11), nullable=False,
                          comment='結合・分割種別(1：「おきたこと」グループ、2：「対応方法」グループ)')
    target_id = Column(BIGINT(20), nullable=False,
                       comment='結合・分割対象の識別子(ケア体験、「対応方法グループ」)')
    from_parent_cluster_id = Column(BIGINT(20), nullable=False, server_default=text(
        "'0'"), comment='結合・分割元「おきたこと」グループ識別子')
    from_child_cluster_id = Column(BIGINT(20), nullable=False, server_default=text(
        "'0'"), comment='結合・分割元「対応方法」グループ識別子')
    from_combine_parent_cluster_id = Column(
        BIGINT(20), nullable=False, comment='結合・分割元結合・分割対象「おきたこと」グループ識別子')
    from_combine_child_cluster_id = Column(
        BIGINT(20), nullable=False, comment='結合・分割元結合・分割対象「対応方法」グループ識別子')
    from_before_happen_represent = Column(
        Text, nullable=False, comment='結合・分割元「おきたこと」代表文(結合・分割前)')
    from_after_happen_represent = Column(
        Text, nullable=False, comment='結合・分割元「おきたこと」代表文(結合・分割後)')
    from_before_cope_represent = Column(
        Text, nullable=False, comment='結合・分割元「対応方法」代表文(結合・分割前)')
    from_after_cope_represent = Column(
        Text, nullable=False, comment='結合・分割元「対応方法」代表文(結合・分割後)')
    to_parent_cluster_id = Column(BIGINT(20), nullable=False, server_default=text(
        "'0'"), comment='結合・分割先「おきたこと」グループ識別子')
    to_child_cluster_id = Column(BIGINT(20), nullable=False, server_default=text(
        "'0'"), comment='結合・分割先「対応方法」グループ識別子')
    to_combine_parent_cluster_id = Column(
        BIGINT(20), nullable=False, comment='結合・分割先結合・分割対象「おきたこと」グループ識別子')
    to_combine_child_cluster_id = Column(
        BIGINT(20), nullable=False, comment='結合・分割先結合・分割対象「対応方法」グループ識別子')
    to_before_happen_represent = Column(
        Text, nullable=False, comment='結合・分割先「おきたこと」代表文(結合・分割前)')
    to_after_happen_represent = Column(
        Text, nullable=False, comment='結合・分割先「おきたこと」代表文(結合・分割後)')
    to_before_cope_represent = Column(
        Text, nullable=False, comment='結合・分割先「対応方法」代表文(結合・分割前)')
    to_after_cope_represent = Column(
        Text, nullable=False, comment='結合・分割先「対応方法」代表文(結合・分割後)')
    to_recommend_flag = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='お勧めフラグ(0：通常、1：お勧め、2：お勧めでない)')
    remarks = Column(Text, nullable=False, comment='備考')

    group_task_group = _relationship('WpGsAdminGroupTaskGroup')


class WpGsAdminGpbpResultMeta(Base):
    __tablename__ = 'wp_gs_admin_gpbp_result_meta'
    __table_args__ = {
        'comment': 'GPBP集計結果に含まれる1件の集計情報。\\r\\n集計結果の表示に必要な情報を格納する。'}

    id = Column(BIGINT(20), primary_key=True, comment='GPBP集計情報ID')
    gpbp_result_id = Column(ForeignKey(
        'wp_gs_admin_gpbp_result.id'), nullable=False, index=True, comment='GPBP集計結果ID')
    parent_cluster_id = Column(
        BIGINT(20), nullable=False, comment='参照元親クラスタID')
    child_cluster_id = Column(BIGINT(20), nullable=False, comment='参照元子クラスタID')
    reason_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='更新状態(0：未更新、1：更新済み、2：承認済み)')
    floormap_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='フロアマップ設定状態(0：未設定、1：設定済み、2：承認済み)')
    belong_posts = Column(Text, nullable=False, comment='所属するケア体験の管理番号')
    happen = Column(Text, nullable=False, comment='おきたこと')
    cope = Column(Text, nullable=False, comment='対応方法')
    gpbp_total = Column(INTEGER(11), nullable=False,
                        server_default=text("'0'"), comment='合計件数')
    gprate = Column(Float, nullable=False, comment='奏功確率')
    reason_gp = Column(Text, nullable=False, comment='うまくいった理由')
    reason_bp = Column(Text, nullable=False, comment='うまくいかなかった理由')
    category = Column(Text, nullable=False, comment='カテゴリ')
    other_category = Column(Text, nullable=False, comment='他にも考えられるカテゴリ')
    floormap_types = Column(Text, nullable=False, comment='フロアマップ種別IDのリスト')
    gpbp_flag = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='GPBPフラグ(0：通常、1：GP、2：BP)')
    recommend_flag = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='お勧めフラグ(0：通常、1：お勧め、2：お勧めでない)')
    keyword = Column(Text, nullable=False, comment='キーワード')
    gp_num = Column(INTEGER(11), nullable=False,
                    server_default=text("'0'"), comment='GP数')
    bp_num = Column(INTEGER(11), nullable=False,
                    server_default=text("'0'"), comment='BP数')
    careinfo_num = Column(INTEGER(11), nullable=False,
                          server_default=text("'0'"), comment='集計情報に含まれるケア体験数')
    gp_careinfo_num = Column(INTEGER(11), nullable=False,
                             server_default=text("'0'"), comment='うまくいったケア体験数')
    bp_careinfo_num = Column(INTEGER(11), nullable=False,
                             server_default=text("'0'"), comment='うまくいかなかったケア体験数')

    gpbp_result = _relationship('WpGsAdminGpbpResult')


class WpGsAdminGroupMember(Base):
    __tablename__ = 'wp_gs_admin_group_members'
    __table_args__ = (
        Index('wp_gs_admin_group_members_idx', 'group_id', 'wp_users_ID'),
    )

    group_member_id = Column(BIGINT(20), primary_key=True, comment='グループメンバID')
    group_id = Column(ForeignKey('wp_gs_admin_group.group_id', ondelete='CASCADE',
                      onupdate='CASCADE'), nullable=False, comment='グループID')
    wp_users_ID = Column(ForeignKey('wp_users.ID', ondelete='CASCADE',
                         onupdate='CASCADE'), nullable=False, index=True, comment='ユーザID')
    member_type = Column(INTEGER(11), nullable=False,
                         server_default=text("'0'"), comment='メンバ種別')

    group = _relationship('WpGsAdminGroup')
    wp_user = _relationship('WpUser')


class WpGsAdminGroupTask(Base):
    __tablename__ = 'wp_gs_admin_group_task'
    __table_args__ = (
        Index('wp_gs_admin_group_task_group_task_group_id_idx',
              'group_task_group_id', 'group_task_id'),
        Index('wp_gs_admin_group_task_idx', 'task_type', 'task_status')
    )

    group_task_id = Column(BIGINT(20), primary_key=True, comment='グループタスクID')
    group_task_group_id = Column(ForeignKey('wp_gs_admin_group_task_group.group_task_group_id',
                                 ondelete='CASCADE', onupdate='CASCADE'), nullable=False, comment='グループタスクグループID')
    group_id = Column(ForeignKey('wp_gs_admin_group.group_id', ondelete='CASCADE',
                      onupdate='CASCADE'), nullable=False, index=True, comment='グループID')
    task_type = Column(INTEGER(11), nullable=False, comment='タスク種別')
    task_status = Column(INTEGER(11), nullable=False,
                         server_default=text("'0'"), comment='タスク状態')
    task_start_date = Column(DateTime, comment='期間開始日')
    task_end_date = Column(DateTime, comment='期間終了日')
    target_id = Column(INTEGER(11), nullable=False,
                       server_default=text("'0'"), comment='グループタスクの対象となる識別子')

    group = _relationship('WpGsAdminGroup')
    group_task_group = _relationship('WpGsAdminGroupTaskGroup')


class WpGsAdminGroupingHappen(Base):
    __tablename__ = 'wp_gs_admin_grouping_happen'
    __table_args__ = (
        Index('wp_gs_admin_grouping_happen_parent_cluster_id_idx',
              'group_task_group_id', 'parent_cluster_id'),
        {'comment': 'おきたことグルーピング情報'}
    )

    id = Column(BIGINT(20), primary_key=True,
                index=True, comment='おきたことグルーピングID')
    group_task_group_id = Column(ForeignKey('wp_gs_admin_group_task_group.group_task_group_id',
                                 ondelete='CASCADE', onupdate='CASCADE'), nullable=False, comment='グループタスクグループID')
    parent_cluster_id = Column(BIGINT(20), nullable=False, server_default=text(
        "'0'"), comment='「おきたこと」グループ識別子')
    happen_represent = Column(Text, nullable=False, comment='「おきたこと」代表文')
    category = Column(Text, nullable=False, comment='カテゴリ')
    other_category = Column(Text, nullable=False, comment='他にも考えられるカテゴリ')

    group_task_group = _relationship('WpGsAdminGroupTaskGroup')


class WpGsAdminGroupingResult(Base):
    __tablename__ = 'wp_gs_admin_grouping_result'
    __table_args__ = (
        Index('wp_gs_admin_grouping_result_idx',
              'group_task_group_id', 'post_id'),
        {'comment': 'グルーピング結果'}
    )

    group_task_group_id = Column(ForeignKey('wp_gs_admin_group_task_group.group_task_group_id',
                                 ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False, comment='グループタスクグループID')
    post_id = Column(BIGINT(20), primary_key=True,
                     nullable=False, comment='ケア体験の管理番号')
    happen_check_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='おきたことグルーピング確認状態')
    cope_check_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='対応方法グルーピング確認状態')
    grouping_happen_id = Column(
        BIGINT(20), nullable=False, server_default=text("'0'"), comment='おきたことグルーピングID')
    grouping_cope_id = Column(
        BIGINT(20), nullable=False, server_default=text("'0'"), comment='対応方法グルーピングID')

    group_task_group = _relationship('WpGsAdminGroupTaskGroup')


class WpGsAdminGroupingUserDictionary(Base):
    __tablename__ = 'wp_gs_admin_grouping_user_dictionary'
    __table_args__ = (
        Index('wp_gs_admin_grouping_user_dictionary_idx',
              'group_task_group_id', 'user_dic_type', 'id'),
        {'comment': 'グルーピング用ユーザ辞書'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='ユーザ辞書ID')
    group_task_group_id = Column(ForeignKey('wp_gs_admin_group_task_group.group_task_group_id',
                                 ondelete='CASCADE', onupdate='CASCADE'), nullable=False, comment='グループタスクグループID')
    user_dic_type = Column(INTEGER(11), nullable=False,
                           comment='ユーザ辞書種別(1：おきたこと、2：対応方法)')
    entry = Column(String(128), nullable=False, comment='表層形')
    left_id = Column(INTEGER(11), nullable=False,
                     server_default=text("'0'"), comment='左文脈ID')
    right_id = Column(INTEGER(11), nullable=False,
                      server_default=text("'0'"), comment='右文脈ID')
    cost = Column(INTEGER(11), nullable=False,
                  server_default=text("'0'"), comment='コスト')
    part = Column(String(64), nullable=False, comment='品詞')
    part_sub_1 = Column(String(64), nullable=False,
                        server_default=text("'*'"), comment='品詞細分類1')
    part_sub_2 = Column(String(64), nullable=False,
                        server_default=text("'*'"), comment='品詞細分類2')
    part_sub_3 = Column(String(64), nullable=False,
                        server_default=text("'*'"), comment='品詞細分類3')
    ctype = Column(String(64), nullable=False,
                   server_default=text("'*'"), comment='活用型')
    cform = Column(String(64), nullable=False,
                   server_default=text("'*'"), comment='活用形')
    original = Column(String(128), nullable=False, comment='原形')
    reading = Column(String(256), nullable=False, comment='読み')
    pronunciation = Column(String(256), nullable=False, comment='発音')

    group_task_group = _relationship('WpGsAdminGroupTaskGroup')


class WpGsBpsdAnswerMeta(Base):
    __tablename__ = 'wp_gs_bpsd_answer_meta'
    __table_args__ = (
        Index('search_wp_gs_bpsd_answer_meta_post_id_idx', 'wp_posts_ID', 'id'),
        Index('search_wp_gs_bpsd_answer_meta_wp_gs_bpsd_meta_post_id_idx',
              'careinfo_post_id', 'answer_number', 'id'),
        {'comment': 'おきたことの対応方法の各属性情報を格納する。'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='おきたことの対応方法ID')
    bpsd_id = Column(ForeignKey('wp_gs_bpsd_meta.id', ondelete='CASCADE',
                     onupdate='CASCADE'), nullable=False, index=True, comment='おきたことID')
    wp_posts_ID = Column(BIGINT(20), nullable=False, comment='おきたことの対応方法の投稿ID')
    careinfo_post_id = Column(BIGINT(20), nullable=False, server_default=text(
        "'0'"), comment='生成したケア体験の投稿ID')
    author_type = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='投稿者種別(1:ケア非実施投稿者、2:ケア実施者)')
    author_detail = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='ケア実施者詳細')
    happen_person = Column(BIGINT(20), comment='認知症のご本人ID')
    cope_happen = Column(LONGTEXT, nullable=False, comment='おこなったこと')
    success_judge = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='結果')
    success_judge_etc = Column(Text, nullable=False, comment='結果のその他テキスト')
    time = Column(Text, nullable=False, comment='時間(複数選択可)')
    time_etc = Column(Text, nullable=False, comment='時間のその他テキスト')
    place = Column(Text, nullable=False, comment='場所(複数選択可)')
    place_etc = Column(Text, nullable=False, comment='場所のその他テキスト')
    cause_happen = Column(Text, nullable=False, comment='症状がおこった原因・理由(複数選択可)')
    cause_happen_etc = Column(Text, nullable=False,
                              comment='症状がおこった原因・理由のその他テキスト')
    reason_good = Column(Text, nullable=False, comment='うまくいった理由(複数選択可)')
    reason_good_etc = Column(Text, nullable=False, comment='うまくいった理由のその他テキスト')
    reason_bad = Column(Text, nullable=False, comment='うまくいかなかった理由')
    reason_bad_etc = Column(Text, nullable=False,
                            comment='うまくいかなかった理由のその他テキスト')
    reason_etc = Column(Text, nullable=False, comment='その他の結果となった理由')
    reason_etc_etc = Column(Text, nullable=False,
                            comment='その他の結果となった理由のその他テキスト')
    weather = Column(Text, nullable=False, comment='天気(複数選択可)')
    weather_etc = Column(Text, nullable=False, comment='天気のその他テキスト')
    impact_event = Column(Text, nullable=False, comment='大きな出来事(複数選択可)')
    impact_event_etc = Column(Text, nullable=False, comment='大きな出来事のその他テキスト')
    worse_symptom = Column(Text, nullable=False, comment='悪化した症状(複数選択可)')
    worse_symptom_etc = Column(Text, nullable=False, comment='悪化した症状のその他テキスト')
    worrisome_event = Column(Text, nullable=False, comment='気になる出来事(複数選択可)')
    worrisome_event_etc = Column(
        Text, nullable=False, comment='気になる出来事のその他テキスト')
    drug_mental = Column(Text, nullable=False, comment='精神や認知に関する薬の変更(複数選択可)')
    drug_mental_etc = Column(Text, nullable=False,
                             comment='精神や認知に関する薬の変更のその他テキスト')
    drug_body = Column(Text, nullable=False, comment='身体に対する薬の変更(複数選択可)')
    drug_body_etc = Column(Text, nullable=False, comment='身体に対する薬の変更その他テキスト')
    etc_text = Column(LONGTEXT, nullable=False, comment='その他')
    answer_number = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='回答番号')

    bpsd = _relationship('WpGsBpsdMeta')


class WpGsBpsdSupportDatum(Base):
    __tablename__ = 'wp_gs_bpsd_support_data'
    __table_args__ = (
        Index('wp_gs_bpsd_support_data_idx', 'manage_id', 'node_no'),
        {'comment': '認知症対応方法発見チャート'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='支援データ番号')
    manage_id = Column(ForeignKey('wp_gs_bpsd_support_manage.id', ondelete='CASCADE',
                       onupdate='CASCADE'), nullable=False, comment='チャート管理番号')
    node_no = Column(INTEGER(11), nullable=False, comment='ノード番号')
    content = Column(Text, comment='内容')
    child_node_no_yes = Column(
        BIGINT(20), nullable=False, server_default=text("'0'"), comment='yesの子ノード番号')
    child_node_no_no = Column(
        BIGINT(20), nullable=False, server_default=text("'0'"), comment='noの子ノード番号')

    manage = _relationship('WpGsBpsdSupportManage')


class WpGsCareinfoCarerInfo(Base):
    __tablename__ = 'wp_gs_careinfo_carer_info'

    id = Column(BIGINT(20), primary_key=True, comment='利用者情報のスナップショットID')
    wp_users_ID = Column(BIGINT(20), nullable=False, comment='利用者ID')
    post_id = Column(ForeignKey('wp_posts.ID', ondelete='CASCADE',
                     onupdate='CASCADE'), nullable=False, index=True, comment='ケア情報の投稿ID')
    carer_id = Column(BIGINT(20), nullable=False, comment='利用者情報ID')
    update_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='更新日')
    user_type = Column(INTEGER(11), nullable=False,
                       server_default=text("'0'"), comment='利用者区分')
    nick_name = Column(Text, nullable=False, comment='ニックネーム')
    gender = Column(INTEGER(11), nullable=False,
                    server_default=text("'0'"), comment='性別')
    birthday_era = Column(INTEGER(11), nullable=False,
                          server_default=text("'0'"), comment='生まれた年[年号]')
    birthday = Column(DateTime, nullable=False, server_default=text(
        "'0000-00-00 00:00:00'"), comment='生まれた年')
    educational_background = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='教育歴：最終学歴')
    educational_background_etc = Column(
        Text, nullable=False, comment='教育歴：最終学歴のその他テキスト')
    educational_duration = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='教育歴：教育年数')
    address_code = Column(Text, nullable=False, comment='住所の郵便番号(最初の3桁)')
    address_prefecture = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='住所の都道府県名')
    job = Column(INTEGER(11), nullable=False,
                 server_default=text("'0'"), comment='職業')
    job_etc = Column(Text, nullable=False, comment='職業のその他テキスト')
    care_duration = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='介護・医療業務歴(年)')
    care_capacity = Column(Text, nullable=False, comment='介護・医療に関する資格(複数選択)')
    care_capacity_etc = Column(
        Text, nullable=False, comment='介護・医療に関する資格のその他テキスト')
    facility_style = Column(INTEGER(11), nullable=False,
                            server_default=text("'0'"), comment='業務施設の様式')
    facility_style_etc = Column(
        Text, nullable=False, comment='業務施設の様式のその他テキスト')
    facility_style_care = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='介護系業務')
    facility_style_care_etc = Column(
        Text, nullable=False, comment='介護系業務のその他テキスト')
    facility_style_medical = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='医療系業務')
    facility_style_medical_etc = Column(
        Text, nullable=False, comment='医療系業務のその他テキスト')
    facility_style_home = Column(
        Text, nullable=False, comment='介護・医療系業務(在宅サービス・外来診療)(複数選択)')
    facility_style_home_etc = Column(
        Text, nullable=False, comment='介護・医療系業務(在宅サービス・外来診療)のその他テキスト')
    facility_style_admission = Column(
        Text, nullable=False, comment='介護・医療系業務(入所サービス・入院診療)(複数選択)')
    facility_style_admission_etc = Column(
        Text, nullable=False, comment='介護・医療系業務(入所サービス・入院診療)のその他テキスト')
    good_care = Column(Text, comment='得意な介護')

    post = _relationship('WpPost')


class WpGsCareinfoDp(Base):
    __tablename__ = 'wp_gs_careinfo_dps'
    __table_args__ = (
        Index('wp_gs_careinfo_dps_user_id_idx', 'wp_users_ID', 'create_date'),
        Index('wp_gs_careinfo_dps_dps_id_idx', 'dps_id', 'id')
    )

    id = Column(BIGINT(20), primary_key=True, index=True,
                comment='認知症のご本人情報のスナップショットID')
    wp_users_ID = Column(BIGINT(20), nullable=False, comment='利用者ID')
    post_id = Column(ForeignKey('wp_posts.ID', ondelete='CASCADE',
                     onupdate='CASCADE'), nullable=False, index=True, comment='ケア情報の投稿ID')
    dps_id = Column(BIGINT(20), nullable=False, comment='認知症のご本人ID')
    create_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='登録日時')
    update_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='更新日時')
    nick_name = Column(Text, nullable=False, comment='認知症のご本人のニックネーム')

    post = _relationship('WpPost')


class WpGsCareinfoDpsMeta(WpGsCareinfoDp):
    __tablename__ = 'wp_gs_careinfo_dps_meta'

    id = Column(ForeignKey('wp_gs_careinfo_dps.id', ondelete='CASCADE', onupdate='CASCADE'),
                primary_key=True, index=True, comment='認知症のご本人情報のスナップショットID')
    relationship = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='認知症のご本人から見たあなたの関係')
    relationship_etc = Column(Text, comment='認知症のご本人から見たあなたの関係のその他テキスト')
    gender = Column(INTEGER(11), nullable=False,
                    server_default=text("'0'"), comment='認知症のご本人の性別')
    birthday_era = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='認知症のご本人の生まれた年[年号]')
    birthday = Column(DateTime, nullable=False, server_default=text(
        "'0000-00-00 00:00:00'"), comment='認知症のご本人の生まれた年')
    address_code = Column(Text, nullable=False,
                          comment='認知症のご本人の住所の郵便番号(最初の3桁)')
    address_prefecture = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='認知症のご本人の住所の都道府県')
    address_prefecture_born = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='認知症のご本人の出生地の都道府県')
    address_prefecture_longstay = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='認知症のご本人が最も長く住んだ都道府県')
    dementia = Column(INTEGER(11), nullable=False,
                      server_default=text("'0'"), comment='認知症の診断の有無')
    cause_disease = Column(Text, nullable=False, comment='認知症の原因疾患(複数選択)')
    cause_disease_etc = Column(Text, comment='認知症の原因疾患のその他テキスト')
    diagnose_doctor = Column(INTEGER(11), nullable=False,
                             server_default=text("'0'"), comment='認知症の診断をした医師')
    diagnose_doctor_etc = Column(Text, comment='認知症の診断をした医師のその他テキスト')
    onset_age = Column(INTEGER(11), nullable=False,
                       server_default=text("'0'"), comment='最初の症状が出た年齢')
    inspection = Column(INTEGER(11), nullable=False,
                        server_default=text("'0'"), comment='認知症検査の実施')
    inspection_mmse_point = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='認知症の検査の得点(MMSE)')
    inspection_hasegawa_point = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='認知症の検査の得点(長谷川式)')
    nursing_level = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='要介護度')
    single_living = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='独居／非独居')
    home_renovation = Column(Text, nullable=False, comment='住宅改修について(複数選択)')
    home_renovation_etc = Column(Text, comment='住宅改修についてのその他テキスト')
    toilet_type = Column(INTEGER(11), nullable=False,
                         server_default=text("'0'"), comment='トイレの洋式・和式について')
    careservice_helper = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：訪問介護(ホームヘルパー)')
    careservice_helper_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：訪問介護(ホームヘルパー)の頻度')
    careservice_nursing = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：訪問看護')
    careservice_nursing_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：訪問看護の頻度')
    careservice_rehabili = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：訪問リハビリ')
    careservice_rehabili_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：訪問リハビリの頻度')
    careservice_dayservice = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：通所介護(デイサービス)')
    careservice_dayservice_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：通所介護(デイサービス)の頻度')
    careservice_daycare = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：通所リハビリ(デイケア)')
    careservice_daycare_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：通所リハビリ(デイケア)の頻度')
    careservice_sstay = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：短期入所生活介護(ショートステイ)')
    careservice_sstay_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：短期入所生活介護(ショートステイ)の頻度')
    careservice_office = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：居宅介護支援事業所')
    careservice_office_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：居宅介護支援事業所の頻度')
    careservice_center = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：地域包括支援センター')
    careservice_center_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：地域包括支援センターの頻度')
    careservice_etc = Column(
        Text, nullable=False, comment='利用している介護サービス(在宅サービス)：その他の介護サービスを詳しく記載してください')
    careservice_admission = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(入所サービス)：施設入所サービス')
    careservice_admission_etc = Column(
        Text, comment='利用している介護サービス(入所サービス)：施設入所サービスのその他テキスト')
    careservice_admission_since = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(入所サービス)：入所してからの日数')
    job = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment=' 認知症のご本人の職業(一番長く就業していた職業)')
    job_etc = Column(Text, comment='認知症のご本人の職業のその他テキスト')
    educational_background = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='教育歴：最終学歴')
    educational_background_etc = Column(Text, comment='教育歴：最終学歴のその他テキスト')
    educational_duration = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='教育歴：教育年数')
    eyesight = Column(INTEGER(11), nullable=False,
                      server_default=text("'0'"), comment='視力')
    eyesight_etc = Column(Text, comment='視力のその他テキスト')
    used_glasses = Column(INTEGER(11), nullable=False,
                          server_default=text("'0'"), comment='眼鏡使用')
    used_glasses_etc = Column(Text, comment='眼鏡使用のその他テキスト')
    hearing = Column(INTEGER(11), nullable=False,
                     server_default=text("'0'"), comment='聴力')
    hearing_etc = Column(Text, comment='聴力のその他テキスト')
    used_aid = Column(INTEGER(11), nullable=False,
                      server_default=text("'0'"), comment='補聴器使用')
    used_aid_etc = Column(Text, comment='補聴器使用のその他テキスト')
    get_up = Column(INTEGER(11), nullable=False,
                    server_default=text("'0'"), comment='起き上がり')
    stand_up = Column(INTEGER(11), nullable=False,
                      server_default=text("'0'"), comment='立ち上がり')
    used_device = Column(Text, nullable=False, comment='使用中の福祉機器(複数選択)')
    used_device_etc = Column(Text, comment='使用中の福祉機器のその他テキスト')
    height = Column(INTEGER(11), comment='身長')
    weight = Column(INTEGER(11), comment='体重')
    handedness = Column(INTEGER(11), nullable=False,
                        server_default=text("'0'"), comment='利き手')
    tooth = Column(INTEGER(11), nullable=False,
                   server_default=text("'0'"), comment='歯')
    tooth_etc = Column(Text, comment='歯のその他テキスト')
    personality_sensitive = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='元々の性格：神経質で些細なことを気にする方である')
    personality_sociability = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='元々の性格：社交的である')
    personality_curiosity = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='元々の性格：好奇心が強い')
    personality_cooperativeness = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='元々の性格：協調性がある')
    personality_diligence = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='元々の性格：勤勉でまじめである')
    personality_pride = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='元々の性格：プライドが高い')
    care_duration = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='あなたが認知症のご本人を介護している年数')
    care_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='あなたと認知症のご本人が会う頻度を教えてください')
    live = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='あなたがお世話している認知症のご本人とあなたの居住形態')
    nursing_fatigue = Column(INTEGER(11), nullable=False,
                             server_default=text("'0'"), comment='あなたの介護疲れ')
    home_care_cost = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='認知症のご本人には、在宅で介護をうけるための経済的余裕がありますか。（ご本人の年金なども含めて）')
    admission_care_cost = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='認知症のご本人には入所してもらうための経済的余裕がありますか。（ご本人の年金なども含めて）')
    main_care = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='あなたは主介護者またはキーパーソンですか？')
    main_care_relationship = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='認知症のご本人から見て主介護者（いない場合はキーパーソン）の続柄は何ですか')
    main_care_relationship_etc = Column(
        Text, comment='認知症のご本人から見て主介護者（いない場合はキーパーソン）の続柄は何ですかのその他テキスト')
    main_care_gender = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='主介護者（キーパーソン）の性別')
    main_care_live = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='主介護者（キーパーソン）との同居/別居について')
    main_care_visitation = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='主介護者（キーパーソン）との面会回数')
    care_member = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='主介護者（キーパーソン）以外に介護支援できる人の存在')
    care_member_etc = Column(
        Text, comment='主介護者（キーパーソン）以外に介護支援できる人の存在のその他テキスト')
    independence_degree_buy = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：買い物')
    independence_degree_buy_etc = Column(Text, comment='日常生活の自立度：買い物のその他テキスト')
    independence_degree_predinner = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='日常生活の自立度：食事を支度すること・料理をつくるという一連の行動')
    independence_degree_predinner_etc = Column(
        Text, comment='日常生活の自立度：食事を支度すること・料理をつくるという一連の行動のその他テキスト')
    independence_degree_eat = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：食事をとること')
    independence_degree_eat_etc = Column(
        Text, comment='日常生活の自立度：食事をとることのその他テキスト')
    independence_degree_washing = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：洗濯')
    independence_degree_washing_etc = Column(
        Text, comment='日常生活の自立度：洗濯のその他テキスト')
    independence_degree_housework = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：上記以外の家事')
    independence_degree_housework_etc = Column(
        Text, comment='日常生活の自立度：上記以外の家事のその他テキスト')
    independence_degree_outing = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：交通手段を使った外出')
    independence_degree_outing_etc = Column(
        Text, comment='日常生活の自立度：交通手段を使った外出のその他テキスト')
    independence_degree_mobility = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：運動機能面からみた移動')
    independence_degree_mobility_etc = Column(
        Text, comment='日常生活の自立度：運動機能面からみた移動のその他テキスト')
    independence_degree_drug = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：服薬の管理')
    independence_degree_drug_etc = Column(
        Text, comment='日常生活の自立度：服薬の管理のその他テキスト')
    independence_degree_money = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：金銭の管理')
    independence_degree_money_etc = Column(
        Text, comment='日常生活の自立度：金銭の管理のその他テキスト')
    independence_degree_tel = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：電話の使い方')
    independence_degree_tel_etc = Column(
        Text, comment='日常生活の自立度：電話の使い方のその他テキスト')
    independence_degree_excretion = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：排泄')
    independence_degree_excretion_etc = Column(
        Text, comment='日常生活の自立度：排泄のその他テキスト')
    independence_degree_clothes = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：着替え')
    independence_degree_clothes_etc = Column(
        Text, comment='日常生活の自立度：着替えのその他テキスト')
    independence_degree_appearance = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='日常生活の自立度：身繕い(身だしなみ、髪や爪の手入れ、洗面など)')
    independence_degree_appearance_etc = Column(
        Text, comment='日常生活の自立度：身繕い(身だしなみ、髪や爪の手入れ、洗面など)のその他テキスト')
    independence_degree_bath = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：入浴')
    independence_degree_bath_etc = Column(Text, comment='日常生活の自立度：入浴のその他テキスト')
    memory_forget = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='最近の出来事を忘れることがありますか？')
    memory_forget_etc = Column(Text, comment='最近の出来事を忘れることがありますか？のその他テキスト')
    memory_judgment = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='日常生活で、ものごとを自分で決める(判断する)ことができますか？')
    memory_judgment_etc = Column(
        Text, comment='日常生活で、ものごとを自分で決める(判断する)ことができますか？のその他テキスト')
    memory_give = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='自分のして欲しいこと、欲しくないことは伝えられますか？')
    memory_give_etc = Column(
        Text, comment='自分のして欲しいこと、欲しくないことは伝えられますか？のその他テキスト')
    independence_result = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='上記の全てを総合的に見てどれにあてはまりますか。')
    independence_result_etc = Column(
        Text, comment='上記の全てを総合的に見てどれにあてはまりますか。のその他テキスト')
    alcohol_drinking = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='アルコールについて：現在あるいは過去のいずれかの時期に')
    illness = Column(Text, comment='これまでにかかった認知症以外の主な病気・治療中の病気：病名')
    illness_etc = Column(Text, comment='これまでにかかった認知症以外の主な病気・治療中の病気：病名のその他テキスト')
    illness_since = Column(
        INTEGER(11), comment='これまでにかかった認知症以外の主な病気・治療中の病気：いつから')
    illness_status = Column(INTEGER(11), server_default=text(
        "'0'"), comment='これまでにかかった認知症以外の主な病気・治療中の病気：現在の状態')
    illness_cancer = Column(
        Text, comment='これまでにかかった認知症以外の主な病気・治療中の病気：がんの部位に対する選択肢(複数選択)')
    illness_cancer_etc = Column(
        Text, comment='これまでにかかった認知症以外の主な病気・治療中の病気：がんの部位に対する選択肢のその他テキスト')
    illness_detail = Column(
        Text, comment='これまでにかかった認知症以外の主な病気・治療中の病気：その他、詳細があれば記載をお願いします。')
    operation = Column(Text, comment='これまでに受けた手術を記載してください。：手術名')
    operation_etc = Column(Text, comment='これまでに受けた手術を記載してください。：手術名のその他テキスト')
    operation_cancer = Column(
        Text, comment='これまでに受けた手術を記載してください。：がんの部位に対する選択肢(複数選択)')
    operation_cancer_etc = Column(
        Text, comment='これまでに受けた手術を記載してください。：がんの部位に対する選択肢のその他テキスト')
    operation_detail = Column(
        Text, comment='これまでに受けた手術を記載してください。：その他、詳細があれば記載をお願いします。')
    close_relative = Column(Text, nullable=False, comment='親しい親族')
    hobby = Column(Text, nullable=False, comment='趣味')
    childhood_memory = Column(LONGTEXT, nullable=False, comment='幼い頃の思い出')
    schoollife_memory = Column(LONGTEXT, nullable=False, comment='学校生活の思い出')
    close_schoolmate = Column(Text, nullable=False, comment='【学校】親しかった友人・先生')
    workplace_relations = Column(
        Text, nullable=False, comment='【職場】上司・同僚・部下など人間関係')
    close_friend = Column(Text, nullable=False, comment='親しい友人')
    favorite_food = Column(Text, nullable=False, comment='好きな食べ物')
    favorite_drink = Column(Text, nullable=False, comment='好きな飲み物')
    dislikes_food = Column(Text, nullable=False, comment='嫌いな食べ物')
    dislikes_drink = Column(Text, nullable=False, comment='嫌いな飲み物')
    favorite_tvprogram = Column(Text, nullable=False, comment='好きなテレビ番組')
    favorite_music = Column(Text, nullable=False, comment='好きな音楽')
    favorite_song = Column(Text, nullable=False, comment='好きな歌')
    favorite_singer = Column(Text, nullable=False, comment='好きな歌手')
    favorite_fragrance = Column(Text, nullable=False, comment='好きな匂い')
    favorite_place = Column(Text, nullable=False, comment='好きな場所')
    knock_touch = Column(Text, nullable=False,
                         comment='お話したり接したりする上でのコツ(こんなことを聞くと喜ばれるなど)あれば')


class WpGsCareinfoMeta(Base):
    __tablename__ = 'wp_gs_careinfo_meta'
    __table_args__ = {'comment': 'ケア情報属性情報'}

    id = Column(BIGINT(20), primary_key=True)
    wp_posts_ID = Column(ForeignKey('wp_posts.ID', ondelete='CASCADE',
                         onupdate='CASCADE'), nullable=False, index=True, comment='ケア情報の投稿ID')
    category_status = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='カテゴリ更新状態(0：未更新、1：更新済み、2：承認済み)')
    author_type = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='投稿者種別(1：ケア非実施投稿者、2：ケア実施者)')
    author_detail = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='ケア実施者詳細')
    happen_person = Column(BIGINT(20), index=True,
                           comment='認知症のご本人(認知症のご本人ID)')
    category = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='①それは、この中のカテゴリでいうと？(カテゴリID)')
    category_etc = Column(Text, nullable=False,
                          comment='①それは、この中のカテゴリでいうと？のその他テキスト')
    original_category = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='入力者が入力したカテゴリ')
    original_category_etc = Column(
        Text, nullable=False, comment='入力者が入力したカテゴリのその他テキスト')
    correct_category = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='正しいカテゴリ')
    correct_category_etc = Column(
        Text, nullable=False, comment='正しいカテゴリのその他テキスト')
    etc_category = Column(Text, nullable=False, comment='他にも考えられるカテゴリ')
    etc_category_etc = Column(Text, nullable=False,
                              comment='他にも考えられるカテゴリのその他テキスト')
    happen = Column(LONGTEXT, nullable=False,
                    comment='②どんなことがおこりましたか？（実際におこったことを簡潔に）')
    cope_happen = Column(LONGTEXT, nullable=False,
                         comment='③これに対してどのように対応しましたか？')
    success_judge = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='④うまくいきましたか？')
    success_judge_etc = Column(
        Text, nullable=False, comment='④うまくいきましたか？のその他テキスト')
    time = Column(Text, nullable=False, comment='①いつ？（困った症状がおきた時間）')
    time_etc = Column(Text, nullable=False,
                      comment='①いつ？（困った症状がおきた時間）のその他テキスト')
    place = Column(Text, nullable=False, comment='②どこで？（困った症状がおきた場所）')
    place_etc = Column(Text, nullable=False,
                       comment='②どこで？（困った症状がおきた場所）のその他テキスト')
    cause_happen = Column(Text, nullable=False, comment='症状がおこった原因・理由')
    cause_happen_etc = Column(Text, nullable=False,
                              comment='症状がおこった原因・理由のその他テキスト')
    reason_good = Column(Text, nullable=False, comment='うまくいった理由')
    reason_good_etc = Column(Text, nullable=False, comment='うまくいった理由のその他テキスト')
    reason_bad = Column(Text, nullable=False, comment='うまくいかなかった理由')
    reason_bad_etc = Column(Text, nullable=False,
                            comment='うまくいかなかった理由のその他テキスト')
    reason_etc = Column(Text, nullable=False, comment='その他の結果となった理由')
    reason_etc_etc = Column(Text, nullable=False,
                            comment='その他の結果となった理由のその他テキスト')
    weather = Column(Text, nullable=False, comment='⑤天気は？（困った症状がおきた時の天気）')
    weather_etc = Column(Text, nullable=False, comment='天気のその他テキスト')
    impact_event = Column(Text, nullable=False, comment='症状の出現や悪化に関係しそうな出来事')
    impact_event_etc = Column(Text, nullable=False,
                              comment='症状の出現や悪化に関係しそうな出来事のその他テキスト')
    worse_symptom = Column(Text, nullable=False, comment='この間に、悪化した他の症状')
    worse_symptom_etc = Column(
        Text, nullable=False, comment='この間に、悪化した他の症状のその他テキスト')
    worrisome_event = Column(Text, nullable=False,
                             comment='この間に、ご本人が気にしていたこと、よく発していた言葉など')
    worrisome_event_etc = Column(
        Text, nullable=False, comment='この間に、ご本人が気にしていたこと、よく発していた言葉などのその他テキスト')
    drug_mental = Column(Text, nullable=False, comment='精神や認知に関する薬の変更')
    drug_mental_etc = Column(Text, nullable=False,
                             comment='精神や認知に関する薬の変更のその他テキスト')
    drug_body = Column(Text, nullable=False, comment='身体に対する薬の変更')
    drug_body_etc = Column(Text, nullable=False, comment='身体に対する薬の変更その他テキスト')
    etc_text = Column(LONGTEXT, nullable=False,
                      comment='その他関連しそうなことがあれば記載してください。')

    wp_post = _relationship('WpPost')


class WpGsCareinfoReaction(Base):
    __tablename__ = 'wp_gs_careinfo_reaction'
    __table_args__ = (
        Index('fk_wp_gs_careinfo_reaction_idx',
              'wp_posts_ID', 'reaction_type'),
        Index('fk_wp_gs_careinfo_reaction_wp_users_idx',
              'wp_posts_ID', 'wp_users_ID'),
        {'comment': 'ケア体験に対するリアクション情報を利用者毎に格納する。'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='ケア体験のリアクションID')
    wp_posts_ID = Column(ForeignKey('wp_posts.ID', ondelete='CASCADE',
                         onupdate='CASCADE'), nullable=False, comment='ケア体験の投稿ID')
    wp_users_ID = Column(BIGINT(20), nullable=False,
                         index=True, comment='利用者ID')
    reaction_type = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='リアクション種別')

    wp_post = _relationship('WpPost')


class WpGsCareinfoVote(Base):
    __tablename__ = 'wp_gs_careinfo_vote'
    __table_args__ = (
        Index('fk_wp_gs_practice_vote_wp_gs_forcare2_idx',
              'wp_posts_ID', 'wp_users_ID'),
        Index('fk_wp_gs_practice_vote_wp_gs_forcare1_idx',
              'wp_posts_ID', 'vote_type'),
        {'comment': 'ケア情報投票情報'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='ケア情報の投票ID')
    wp_posts_ID = Column(ForeignKey('wp_posts.ID', ondelete='CASCADE',
                         onupdate='CASCADE'), nullable=False, comment='ケア情報の投稿ID')
    wp_users_ID = Column(BIGINT(20), nullable=False,
                         index=True, comment='利用者ID')
    vote_type = Column(INTEGER(11), nullable=False,
                       server_default=text("'0'"), comment='投票種別(GP/BP)')

    wp_post = _relationship('WpPost')


class WpGsDementiaPerson(Base):
    __tablename__ = 'wp_gs_dementia_person'
    __table_args__ = (
        Index('type_user_id', 'wp_users_ID', 'id'),
        Index('wp_gs_dementia_person_carer_id_idx', 'carer_id', 'id'),
        {'comment': '認知症のご本人情報'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='認知症のご本人ID')
    wp_users_ID = Column(BIGINT(20), nullable=False, comment='利用者ID')
    carer_id = Column(ForeignKey('wp_gs_carer_info.id', ondelete='CASCADE',
                      onupdate='CASCADE'), nullable=False, comment='利用者情報ID')
    status = Column(String(20), nullable=False, comment='公開状態')
    create_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='登録日時')
    update_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='更新日時')
    notice_date = Column(DateTime, comment='更新通知日時')
    nick_name = Column(Text, nullable=False, comment='認知症のご本人のニックネーム')

    carer = _relationship('WpGsCarerInfo')


class WpGsGpbpSummary(Base):
    __tablename__ = 'wp_gs_gpbp_summary'
    __table_args__ = (
        Index('wp_gs_gpbp_summary_happen_total_idx',
              'summary_manage_id', 'parent_cluster_id'),
        {'comment': 'GPBP集計結果公開情報'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='GPBP集計結果ID')
    summary_manage_id = Column(ForeignKey('wp_gs_gpbp_summary_manage.id', ondelete='CASCADE',
                               onupdate='CASCADE'), nullable=False, comment='GPBP集計結果公開管理ID')
    gpbp_result_meta_id = Column(
        BIGINT(20), nullable=False, comment='GPBP集計情報ID')
    parent_cluster_id = Column(BIGINT(20), nullable=False, server_default=text(
        "'0'"), comment='「おきたこと」グループ識別子')
    category = Column(Text, nullable=False, comment='カテゴリ')
    keyword = Column(Text, nullable=False, comment='キーワード')
    happen = Column(Text, nullable=False, comment='おきたこと')
    cope = Column(Text, nullable=False, comment='対応')
    gpnum = Column(INTEGER(11), nullable=False,
                   server_default=text("'0'"), comment='うまくいった件数')
    bpnum = Column(INTEGER(11), nullable=False,
                   server_default=text("'0'"), comment='うまくいかなかった件数')
    gprate = Column(Float, nullable=False,
                    server_default=text("'0'"), comment='奏功確率')
    gpreason = Column(Text, nullable=False, comment='うまくいった理由')
    bpreason = Column(Text, nullable=False, comment='うまくいかなかった理由')
    flag = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='GPBPフラグ(0：通常、1：GP、2：BP)')
    recommend_flag = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='お勧めフラグ(0：通常、1：お勧め、2：お勧めでない)')
    visible = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='表示フラグ(0：非表示、1：表示)')
    careinfo_list = Column(Text, nullable=False, comment='ケア体験IDのリスト')

    summary_manage = _relationship('WpGsGpbpSummaryManage')


class WpGsGpbpSummaryFloormap(Base):
    __tablename__ = 'wp_gs_gpbp_summary_floormap'
    __table_args__ = (
        Index('wp_gs_gpbp_summary_floormap_happen_total_idx',
              'summary_manage_id', 'parent_cluster_id'),
        {'comment': 'GPBP集計結果公開情報(フロアマップ)'}
    )

    id = Column(BIGINT(20), primary_key=True, comment='GPBP集計結果(フロアマップ)ID')
    summary_manage_id = Column(ForeignKey('wp_gs_gpbp_summary_manage.id', ondelete='CASCADE',
                               onupdate='CASCADE'), nullable=False, comment='GPBP集計結果公開管理ID')
    gpbp_result_meta_id = Column(
        BIGINT(20), nullable=False, comment='GPBP集計情報ID')
    floormap_group = Column(Text, nullable=False, comment='フロアマップ属性グループ')
    parent_cluster_id = Column(BIGINT(20), nullable=False, server_default=text(
        "'0'"), comment='「おきたこと」グループ識別子')
    category = Column(Text, nullable=False, comment='カテゴリ')
    keyword = Column(Text, nullable=False, comment='キーワード')
    happen = Column(Text, nullable=False, comment='おきたこと')
    cope = Column(Text, nullable=False, comment='対応方法')
    gpnum = Column(INTEGER(11), nullable=False,
                   server_default=text("'0'"), comment='うまくいった件数')
    bpnum = Column(INTEGER(11), nullable=False,
                   server_default=text("'0'"), comment='うまくいかなかった件数')
    gprate = Column(Float, nullable=False,
                    server_default=text("'0'"), comment='奏功確率')
    gpreason = Column(Text, nullable=False, comment='うまくいった理由')
    bpreason = Column(Text, nullable=False, comment='うまくいかなかった理由')
    flag = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='GPBPフラグ(0：通常、1：GP、2：BP)')
    recommend_flag = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='お勧めフラグ(0：通常、1：お勧め、2：お勧めでない)')
    visible = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='表示フラグ(0：非表示、1：表示)')
    careinfo_list = Column(Text, nullable=False, comment='ケア体験IDのリスト')

    summary_manage = _relationship('WpGsGpbpSummaryManage')


class WpGsMetaCategory(Base):
    __tablename__ = 'wp_gs_meta_categories'
    __table_args__ = (
        Index('sorted_wp_gs_meta_categories_idx',
              'wp_gs_meta_type_id', 'position', 'id'),
    )

    id = Column(BIGINT(20), primary_key=True, comment='入力項目のカテゴリID')
    wp_gs_meta_type_id = Column(ForeignKey(
        'wp_gs_meta_type.id'), nullable=False, index=True, comment='入力を行う情報種別')
    category_name = Column(String(128), nullable=False,
                           comment='カテゴリを分けるdivタグのidに利用するカテゴリ名称')
    category_type = Column(INTEGER(11), nullable=False, comment='カテゴリの表示種別')
    category_label = Column(Text, comment='カテゴリのラベル')
    category_description = Column(Text, comment='カテゴリの説明')
    category_help = Column(Text, comment='ヘルプ用のメッセージを設定する')
    effect_class = Column(String(128), comment='カテゴリにクラス名を付与してcssで制御するための設定値')
    required = Column(INTEGER(11), server_default=text("'0'"), comment='必須フラグ')
    position = Column(INTEGER(11), nullable=False, server_default=text(
        "'100'"), comment='カテゴリの表示順を設定する(ソート用)')

    wp_gs_meta_type = _relationship('WpGsMetaType')


class WpGsAdminCombineCareinfo(Base):
    __tablename__ = 'wp_gs_admin_combine_careinfo'
    __table_args__ = (
        Index('wp_gs_admin_combine_careinfo_idx', 'group_task_group_id',
              'combine_parent_cluster_id', 'combine_child_cluster_id', 'post_id'),
        {'comment': '結合・分割対象ケア体験情報'}
    )

    post_id = Column(BIGINT(20), primary_key=True,
                     nullable=False, comment='ケア体験管理番号')
    group_task_group_id = Column(
        BIGINT(20), primary_key=True, nullable=False, comment='グループタスクグループID')
    combine_parent_cluster_id = Column(ForeignKey('wp_gs_admin_combine_parent_cluster.id', ondelete='CASCADE',
                                       onupdate='CASCADE'), nullable=False, index=True, comment='結合・分割対象「おきたこと」グループ識別子')
    combine_child_cluster_id = Column(ForeignKey('wp_gs_admin_combine_child_cluster.id', ondelete='CASCADE',
                                      onupdate='CASCADE'), nullable=False, index=True, comment='結合・分割対象「対応方法」グループ識別子')
    happen = Column(Text, comment='おきたこと')
    cope = Column(Text, comment='対応方法')
    category = Column(Text, comment='カテゴリ')
    other_category = Column(Text, comment='他にも考えられるカテゴリ')

    combine_child_cluster = _relationship('WpGsAdminCombineChildCluster')
    combine_parent_cluster = _relationship('WpGsAdminCombineParentCluster')


class WpGsAdminGroupingHappenRule(Base):
    __tablename__ = 'wp_gs_admin_grouping_happen_rules'
    __table_args__ = (
        Index('wp_gs_admin_grouping_happen_rules_idx',
              'grouping_happen_id', 'row'),
        {'comment': 'おきたことグルーピングルール'}
    )

    grouping_happen_id = Column(ForeignKey('wp_gs_admin_grouping_happen.id', ondelete='CASCADE',
                                onupdate='CASCADE'), primary_key=True, nullable=False, comment='おきたことグルーピングID')
    row = Column(INTEGER(11), primary_key=True, nullable=False, comment='行番号')
    value = Column(Text, nullable=False, comment='要素')
    importance = Column(INTEGER(11), nullable=False,
                        server_default=text("'0'"), comment='重要度')

    grouping_happen = _relationship('WpGsAdminGroupingHappen')


class WpGsAdminGroupingResultHappen(Base):
    __tablename__ = 'wp_gs_admin_grouping_result_happen'
    __table_args__ = (
        ForeignKeyConstraint(['group_task_group_id', 'post_id'], ['wp_gs_admin_grouping_result.group_task_group_id',
                             'wp_gs_admin_grouping_result.post_id'], ondelete='CASCADE', onupdate='CASCADE'),
        Index('wp_gs_admin_grouping_result_happen_idx',
              'group_task_group_id', 'post_id', 'grouping_happen_id'),
        {'comment': 'おきたことグルーピング結果'}
    )

    group_task_group_id = Column(
        BIGINT(20), primary_key=True, nullable=False, comment='グループタスクグループID')
    post_id = Column(BIGINT(20), primary_key=True,
                     nullable=False, comment='ケア体験の管理番号')
    grouping_happen_id = Column(BIGINT(
        20), primary_key=True, nullable=False, server_default=text("'0'"), comment='おきたことグルーピングID')
    accuracy = Column(INTEGER(11), nullable=False,
                      server_default=text("'0'"), comment='確度')
    feature = Column(INTEGER(11), nullable=False,
                     server_default=text("'0'"), comment='特徴度')

    group_task_group = _relationship('WpGsAdminGroupingResult')


class WpGsAdminResultMorphoLogical(Base):
    __tablename__ = 'wp_gs_admin_result_morpho_logical'
    __table_args__ = (
        ForeignKeyConstraint(['group_task_group_id', 'post_id'], ['wp_gs_admin_grouping_result.group_task_group_id',
                             'wp_gs_admin_grouping_result.post_id'], ondelete='CASCADE', onupdate='CASCADE'),
        Index('wp_gs_admin_result_morpho_logical_idx',
              'morpho_logical_type', 'word_id'),
        {'comment': '形態素解析結果'}
    )

    group_task_group_id = Column(
        BIGINT(20), primary_key=True, nullable=False, comment='グループタスクグループID')
    post_id = Column(BIGINT(20), primary_key=True,
                     nullable=False, comment='ケア体験の管理番号')
    morpho_logical_type = Column(INTEGER(
        11), primary_key=True, nullable=False, comment='形態素解析種別(1：おきたこと、2：対応方法)')
    word_id = Column(BIGINT(20), primary_key=True,
                     nullable=False, comment='単語ID')
    surface = Column(String(128), nullable=False, comment='表層形(見出し語)')
    original = Column(String(128), nullable=False, comment='原形')
    part = Column(String(64), nullable=False,
                  server_default=text("'*'"), comment='品詞')
    part_sub_1 = Column(String(64), nullable=False,
                        server_default=text("'*'"), comment='品詞詳細1')
    part_sub_2 = Column(String(64), nullable=False,
                        server_default=text("'*'"), comment='品詞詳細2')
    part_sub_3 = Column(String(64), nullable=False,
                        server_default=text("'*'"), comment='品詞詳細3')
    ctype = Column(String(64), nullable=False,
                   server_default=text("'*'"), comment='活用型')
    cform = Column(String(64), nullable=False,
                   server_default=text("'*'"), comment='活用形')
    reading = Column(String(256), nullable=False,
                     server_default=text("'*'"), comment='読み')
    pronunciation = Column(String(256), nullable=False,
                           server_default=text("'*'"), comment='発音')
    left_id = Column(INTEGER(11), nullable=False,
                     server_default=text("'0'"), comment='左文脈ID')
    right_id = Column(INTEGER(11), nullable=False,
                      server_default=text("'0'"), comment='右文脈ID')
    cost = Column(INTEGER(11), nullable=False,
                  server_default=text("'0'"), comment='コスト')

    group_task_group = _relationship('WpGsAdminGroupingResult')


class WpGsDementiaPersonMetaBasic(Base):
    __tablename__ = 'wp_gs_dementia_person_meta_basic'
    __table_args__ = (
        Index('wp_gs_dementia_person_meta_basic_status_idx',
              'wp_gs_dementia_person_id', 'id', 'status'),
    )

    id = Column(BIGINT(20), primary_key=True, comment='認知症のご本人基本情報ID')
    wp_gs_dementia_person_id = Column(ForeignKey(
        'wp_gs_dementia_person.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, comment='認知症のご本人ID')
    status = Column(String(20), comment='公開状態')
    update_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='更新日')
    job = Column(INTEGER(11), nullable=False,
                 server_default=text("'0'"), comment='認知症のご本人の職業')
    job_etc = Column(Text, comment='認知症のご本人の職業のその他テキスト')
    educational_background = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='教育歴')
    educational_background_etc = Column(Text, comment='教育歴のその他テキスト')
    educational_duration = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='教育年数')
    eyesight = Column(INTEGER(11), nullable=False,
                      server_default=text("'0'"), comment='視力')
    eyesight_etc = Column(Text, comment='視力のその他テキスト')
    used_glasses = Column(INTEGER(11), nullable=False,
                          server_default=text("'0'"), comment='眼鏡使用')
    used_glasses_etc = Column(Text, comment='眼鏡使用のその他テキスト')
    hearing = Column(INTEGER(11), nullable=False,
                     server_default=text("'0'"), comment='聴力')
    hearing_etc = Column(Text, comment='聴力のその他テキスト')
    used_aid = Column(INTEGER(11), nullable=False,
                      server_default=text("'0'"), comment='補聴器使用')
    used_aid_etc = Column(Text, comment='補聴器使用のその他テキスト')
    get_up = Column(INTEGER(11), nullable=False,
                    server_default=text("'0'"), comment='起き上がり')
    stand_up = Column(INTEGER(11), nullable=False,
                      server_default=text("'0'"), comment='立ち上がり')
    used_device = Column(Text, nullable=False, comment='使用中の福祉機器など(複数選択)')
    used_device_etc = Column(Text, comment='使用中の福祉機器などのその他テキスト')
    height = Column(INTEGER(11), comment='身長')
    weight = Column(INTEGER(11), comment='体重')
    handedness = Column(INTEGER(11), nullable=False,
                        server_default=text("'0'"), comment='利き手')
    tooth = Column(INTEGER(11), nullable=False,
                   server_default=text("'0'"), comment='歯')
    tooth_etc = Column(Text, comment='歯のその他テキスト')
    address_prefecture_born = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='認知症のご本人の出生地の都道府県')
    address_prefecture_longstay = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='認知症のご本人が最も長く住んだ都道府県')

    wp_gs_dementia_person = _relationship('WpGsDementiaPerson')


class WpGsDementiaPersonMetaCare(Base):
    __tablename__ = 'wp_gs_dementia_person_meta_care'
    __table_args__ = (
        Index('wp_gs_dementia_person_meta_care_status_idx',
              'wp_gs_dementia_person_id', 'id', 'status'),
    )

    id = Column(BIGINT(20), primary_key=True, comment='認知症のご本人介護情報ID')
    wp_gs_dementia_person_id = Column(ForeignKey(
        'wp_gs_dementia_person.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, comment='認知症のご本人ID')
    status = Column(String(20), comment='公開状態')
    update_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='更新日')
    care_duration = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='認知症の介護歴')
    care_status = Column(INTEGER(11), nullable=False,
                         server_default=text("'0'"), comment='介護状況')
    live = Column(INTEGER(11), nullable=False,
                  server_default=text("'0'"), comment='認知症のご本人との居住形態')
    nursing_fatigue = Column(INTEGER(11), nullable=False,
                             server_default=text("'0'"), comment='介護疲れ')
    home_care_cost = Column(INTEGER(11), nullable=False,
                            server_default=text("'0'"), comment='在宅介護費用について')
    admission_care_cost = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='入所介護費用について')

    wp_gs_dementia_person = _relationship('WpGsDementiaPerson')


class WpGsDementiaPersonMetaCareService(Base):
    __tablename__ = 'wp_gs_dementia_person_meta_care_service'
    __table_args__ = (
        Index('wp_gs_dementia_person_meta_care_service_status_idx',
              'wp_gs_dementia_person_id', 'id', 'status'),
    )

    id = Column(BIGINT(20), primary_key=True, comment='認知症のご本人介護サービスID')
    wp_gs_dementia_person_id = Column(ForeignKey(
        'wp_gs_dementia_person.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, comment='認知症のご本人ID')
    status = Column(String(20), comment='公開状態')
    update_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='更新日')
    nursing_level = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='要介護度')
    single_living = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='独居／非独居')
    home_renovation = Column(Text, nullable=False, comment='住宅改修について(複数選択)')
    home_renovation_etc = Column(Text, comment='住宅改修についてのその他テキスト')
    toilet_type = Column(INTEGER(11), nullable=False,
                         server_default=text("'0'"), comment='トイレの洋式・和式について')
    careservice_helper = Column(INTEGER(11), nullable=False, server_default=text(
        "'1'"), comment='利用している介護サービス(在宅サービス)：訪問介護(ホームヘルパー)')
    careservice_helper_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：訪問介護(ホームヘルパー)の頻度')
    careservice_nursing = Column(INTEGER(11), nullable=False, server_default=text(
        "'1'"), comment='利用している介護サービス(在宅サービス)：訪問看護')
    careservice_nursing_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：訪問看護の頻度')
    careservice_rehabili = Column(INTEGER(11), nullable=False, server_default=text(
        "'1'"), comment='利用している介護サービス(在宅サービス)：訪問リハビリ')
    careservice_rehabili_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：訪問リハビリの頻度')
    careservice_dayservice = Column(INTEGER(11), nullable=False, server_default=text(
        "'1'"), comment='利用している介護サービス(在宅サービス)：通所介護(デイサービス)')
    careservice_dayservice_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：通所介護(デイサービス)の頻度')
    careservice_daycare = Column(INTEGER(11), nullable=False, server_default=text(
        "'1'"), comment='利用している介護サービス(在宅サービス)：通所リハビリ(デイケア)')
    careservice_daycare_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：通所リハビリ(デイケア)の頻度')
    careservice_sstay = Column(INTEGER(11), nullable=False, server_default=text(
        "'1'"), comment='利用している介護サービス(在宅サービス)：短期入所生活介護(ショートステイ)')
    careservice_sstay_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：短期入所生活介護(ショートステイ)の頻度')
    careservice_office = Column(INTEGER(11), nullable=False, server_default=text(
        "'1'"), comment='利用している介護サービス(在宅サービス)：居宅介護支援事業所')
    careservice_office_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：居宅介護支援事業所の頻度')
    careservice_center = Column(INTEGER(11), nullable=False, server_default=text(
        "'1'"), comment='利用している介護サービス(在宅サービス)：地域包括支援センター')
    careservice_center_frequency = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(在宅サービス)：地域包括支援センターの頻度')
    careservice_etc = Column(Text, nullable=False,
                             comment='利用している介護サービス(在宅サービス)：その他')
    careservice_admission = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(入所サービス)：入所施設')
    careservice_admission_etc = Column(
        Text, comment='利用している介護サービス(入所サービス)：入所施設のその他テキスト')
    careservice_admission_since = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='利用している介護サービス(入所サービス)：入所してからの日数')

    wp_gs_dementia_person = _relationship('WpGsDementiaPerson')


class WpGsDementiaPersonMetaDementia(Base):
    __tablename__ = 'wp_gs_dementia_person_meta_dementia'
    __table_args__ = (
        Index('wp_gs_dementia_person_meta_dementia_status_idx',
              'wp_gs_dementia_person_id', 'id', 'status'),
    )

    id = Column(BIGINT(20), primary_key=True, comment='認知症のご本人認知症関連ID')
    wp_gs_dementia_person_id = Column(ForeignKey(
        'wp_gs_dementia_person.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, comment='認知症のご本人ID')
    status = Column(String(20), comment='公開状態')
    update_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='更新日')
    dementia = Column(INTEGER(11), nullable=False,
                      server_default=text("'0'"), comment='認知症の診断の有無')
    cause_disease = Column(Text, nullable=False, comment='認知症の原因疾患(複数選択)')
    cause_disease_etc = Column(Text, comment='認知症の原因疾患のその他テキスト')
    diagnose_doctor = Column(INTEGER(11), nullable=False,
                             server_default=text("'0'"), comment='認知症の診断をした医師')
    diagnose_doctor_etc = Column(Text, comment='認知症の診断をした医師のその他テキスト')
    onset_age = Column(INTEGER(11), nullable=False,
                       server_default=text("'0'"), comment='最初の症状が出た年齢')
    inspection = Column(INTEGER(11), nullable=False,
                        server_default=text("'0'"), comment='認知検査の施行')
    inspection_mmse_point = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='認知検査の得点(MMSE)')
    inspection_hasegawa_point = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='認知検査の得点(長谷川式)')

    wp_gs_dementia_person = _relationship('WpGsDementiaPerson')


class WpGsDementiaPersonMetaEtc(Base):
    __tablename__ = 'wp_gs_dementia_person_meta_etc'
    __table_args__ = (
        Index('wp_gs_dementia_person_meta_etc_status_idx',
              'wp_gs_dementia_person_id', 'id', 'status'),
    )

    id = Column(BIGINT(20), primary_key=True, comment='認知症のご本人基本情報ID')
    wp_gs_dementia_person_id = Column(ForeignKey(
        'wp_gs_dementia_person.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, comment='認知症のご本人ID')
    status = Column(String(20), comment='公開状態')
    update_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='更新日')
    close_relative = Column(Text, nullable=False, comment='親しい親族')
    hobby = Column(Text, nullable=False, comment='趣味')
    childhood_memory = Column(LONGTEXT, nullable=False, comment='幼い頃の思い出')
    schoollife_memory = Column(LONGTEXT, nullable=False, comment='学校生活の思い出')
    close_schoolmate = Column(Text, nullable=False, comment='【学校】親しかった友人・先生')
    workplace_relations = Column(
        Text, nullable=False, comment='【職場】上司・同僚・部下など人間関係')
    close_friend = Column(Text, nullable=False, comment='親しい友人')
    favorite_food = Column(Text, nullable=False, comment='好きな食べ物')
    favorite_drink = Column(Text, nullable=False, comment='好きな飲み物')
    dislikes_food = Column(Text, nullable=False, comment='嫌いな食べ物')
    dislikes_drink = Column(Text, nullable=False, comment='嫌いな飲み物')
    favorite_tvprogram = Column(Text, nullable=False, comment='好きなテレビ番組')
    favorite_music = Column(Text, nullable=False, comment='好きな音楽')
    favorite_song = Column(Text, nullable=False, comment='好きな歌')
    favorite_singer = Column(Text, nullable=False, comment='好きな歌手')
    favorite_fragrance = Column(Text, nullable=False, comment='好きな匂い')
    favorite_place = Column(Text, nullable=False, comment='好きな場所')
    knock_touch = Column(Text, nullable=False,
                         comment='お話したり接したりする上でのコツ(こんなことを聞くと喜ばれるなど)あれば')

    wp_gs_dementia_person = _relationship('WpGsDementiaPerson')


class WpGsDementiaPersonMetaIllnes(Base):
    __tablename__ = 'wp_gs_dementia_person_meta_illness'
    __table_args__ = (
        Index('wp_gs_dementia_person_meta_illness_status_idx',
              'wp_gs_dementia_person_id', 'id', 'status'),
    )

    id = Column(BIGINT(20), primary_key=True, comment='認知症のご本人認知症関連ID')
    wp_gs_dementia_person_id = Column(ForeignKey(
        'wp_gs_dementia_person.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, comment='認知症のご本人ID')
    status = Column(String(20), comment='公開状態')
    update_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='更新日')
    alcohol_drinking = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='アルコールについて：飲酒の有無、頻度')
    illness = Column(Text, comment='これまでにかかった認知症以外の主な病気(複数選択)')
    illness_etc = Column(Text, comment='これまでにかかった認知症以外の主な病気のその他テキスト')
    illness_status = Column(INTEGER(11), server_default=text(
        "'0'"), comment='これまでにかかった認知症以外の主な病気：現在の状態')
    illness_cancer = Column(Text, comment='がんの部位に対する選択肢(複数選択)')
    illness_cancer_etc = Column(Text, comment='がんの部位に対する選択肢のその他テキスト')
    illness_detail = Column(Text, comment='その他の詳細')
    operation = Column(Text, comment='これまでに受けた手術')
    operation_etc = Column(Text, comment='これまでに受けた手術その他テキスト')
    operation_cancer = Column(Text, comment='がんの部位に対する選択肢(複数選択)')
    operation_cancer_etc = Column(Text, comment='がんの部位に対する選択肢のその他テキスト')
    operation_detail = Column(Text, comment='その他の詳細')

    wp_gs_dementia_person = _relationship('WpGsDementiaPerson')


class WpGsDementiaPersonMetaIndependence(Base):
    __tablename__ = 'wp_gs_dementia_person_meta_independence'
    __table_args__ = (
        Index('wp_gs_dementia_person_meta_independence_status_idx',
              'wp_gs_dementia_person_id', 'id', 'status'),
    )

    id = Column(BIGINT(20), primary_key=True, comment='認知症のご本人認知症関連ID')
    wp_gs_dementia_person_id = Column(ForeignKey(
        'wp_gs_dementia_person.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, comment='認知症のご本人ID')
    status = Column(String(20), comment='公開状態')
    update_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='更新日')
    independence_degree_buy = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：買い物')
    independence_degree_buy_etc = Column(Text, comment='日常生活の自立度：買い物のその他テキスト')
    independence_degree_predinner = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：食事の支度')
    independence_degree_predinner_etc = Column(
        Text, comment='日常生活の自立度：食事の支度のその他テキスト')
    independence_degree_eat = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：食事')
    independence_degree_eat_etc = Column(Text, comment='日常生活の自立度：食事のその他テキスト')
    independence_degree_washing = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：洗濯')
    independence_degree_washing_etc = Column(
        Text, comment='日常生活の自立度：洗濯のその他テキスト')
    independence_degree_housework = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：上記以外の家事')
    independence_degree_housework_etc = Column(
        Text, comment='日常生活の自立度：上記以外の家事のその他テキスト')
    independence_degree_outing = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：移動・外出')
    independence_degree_outing_etc = Column(
        Text, comment='日常生活の自立度：移動・外出のその他テキスト')
    independence_degree_mobility = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：移動能力')
    independence_degree_mobility_etc = Column(
        Text, comment='日常生活の自立度：移動能力のその他テキスト')
    independence_degree_drug = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：服薬の管理')
    independence_degree_drug_etc = Column(
        Text, comment='日常生活の自立度：服薬の管理のその他テキスト')
    independence_degree_money = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：金銭の管理')
    independence_degree_money_etc = Column(
        Text, comment='日常生活の自立度：金銭の管理のその他テキスト')
    independence_degree_tel = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：電話の使い方')
    independence_degree_tel_etc = Column(
        Text, comment='日常生活の自立度：電話の使い方のその他テキスト')
    independence_degree_excretion = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：排泄')
    independence_degree_excretion_etc = Column(
        Text, comment='日常生活の自立度：排泄のその他テキスト')
    independence_degree_clothes = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：着替え')
    independence_degree_clothes_etc = Column(
        Text, comment='日常生活の自立度：着替えのその他テキスト')
    independence_degree_appearance = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：見繕い')
    independence_degree_appearance_etc = Column(
        Text, comment='日常生活の自立度：見繕いのその他テキスト')
    independence_degree_bath = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='日常生活の自立度：入浴')
    independence_degree_bath_etc = Column(Text, comment='日常生活の自立度：入浴のその他テキスト')
    memory_forget = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='理解および記憶：忘れることがある')
    memory_forget_etc = Column(Text, comment='理解および記憶：忘れることがあるのその他テキスト')
    memory_judgment = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='理解および記憶：判断することができる')
    memory_judgment_etc = Column(Text, comment='理解および記憶：判断することができるのその他テキスト')
    memory_give = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='理解および記憶：伝えることができる')
    memory_give_etc = Column(Text, comment='理解および記憶：伝えることができるのその他テキスト')
    independence_result = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='総合')
    independence_result_etc = Column(Text, comment='総合のその他テキスト')

    wp_gs_dementia_person = _relationship('WpGsDementiaPerson')


class WpGsDementiaPersonMetaMainCare(Base):
    __tablename__ = 'wp_gs_dementia_person_meta_main_care'
    __table_args__ = (
        Index('wp_gs_dementia_person_meta_main_care_status_idx',
              'wp_gs_dementia_person_id', 'id', 'status'),
    )

    id = Column(BIGINT(20), primary_key=True, comment='認知症のご本人主介護者情報ID')
    wp_gs_dementia_person_id = Column(ForeignKey(
        'wp_gs_dementia_person.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, comment='認知症のご本人ID')
    status = Column(String(20), comment='公開状態')
    update_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='更新日')
    main_care = Column(INTEGER(11), nullable=False,
                       server_default=text("'0'"), comment='主介護者、またはキーパーソン')
    main_care_relationship = Column(INTEGER(
        11), nullable=False, server_default=text("'0'"), comment='認知症のご本人から見た主介護者の続柄')
    main_care_relationship_etc = Column(
        Text, comment='認知症のご本人から見た主介護者の続柄のその他テキスト')
    main_care_gender = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='主介護者の性別')
    main_care_live = Column(INTEGER(11), nullable=False,
                            server_default=text("'0'"), comment='主介護者との同居の有無')
    main_care_visitation = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='主介護者との面会回数')
    care_member = Column(INTEGER(11), nullable=False,
                         server_default=text("'0'"), comment='主介護者以外に介護支援できる人')
    care_member_etc = Column(Text, comment='主介護者以外に介護支援できる人のその他テキスト')

    wp_gs_dementia_person = _relationship('WpGsDementiaPerson')


class WpGsDementiaPersonMetaOption(Base):
    __tablename__ = 'wp_gs_dementia_person_meta_option'
    __table_args__ = (
        Index('wp_gs_dementia_person_meta_option_index',
              'wp_gs_dementia_person_id', 'meta_category_name', 'meta_field_name'),
    )

    wp_gs_dementia_person_id = Column(ForeignKey('wp_gs_dementia_person.id', ondelete='CASCADE',
                                      onupdate='CASCADE'), primary_key=True, nullable=False, comment='認知症のご本人ID')
    meta_field_name = Column(
        String(192), primary_key=True, nullable=False, comment='入力項目のフィールド名')
    meta_category_name = Column(
        String(128), nullable=False, comment='入力項目のカテゴリ名')
    value = Column(Text, comment='特殊な設定値')

    wp_gs_dementia_person = _relationship('WpGsDementiaPerson')


class WpGsDementiaPersonMetaPersonality(Base):
    __tablename__ = 'wp_gs_dementia_person_meta_personality'
    __table_args__ = (
        Index('wp_gs_dementia_person_meta_personality_status_idx',
              'wp_gs_dementia_person_id', 'id', 'status'),
    )

    id = Column(BIGINT(20), primary_key=True, comment='認知症のご本人性格情報ID')
    wp_gs_dementia_person_id = Column(ForeignKey(
        'wp_gs_dementia_person.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, comment='認知症のご本人ID')
    status = Column(String(20), comment='公開状態')
    update_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='更新日')
    personality_sensitive = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='元々の性格：神経症傾向')
    personality_sociability = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='元々の性格：社交性')
    personality_curiosity = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='元々の性格：好奇心')
    personality_cooperativeness = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='元々の性格：協調性')
    personality_diligence = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='元々の性格：勤勉性')
    personality_pride = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='元々の性格：プライド')

    wp_gs_dementia_person = _relationship('WpGsDementiaPerson')


class WpGsDementiaPersonMetaRequired(Base):
    __tablename__ = 'wp_gs_dementia_person_meta_required'
    __table_args__ = (
        Index('wp_gs_dementia_person_meta_required_status_idx',
              'wp_gs_dementia_person_id', 'id', 'status'),
    )

    id = Column(BIGINT(20), primary_key=True, comment='認知症のご本人必須情報ID')
    wp_gs_dementia_person_id = Column(ForeignKey(
        'wp_gs_dementia_person.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, comment='認知症のご本人ID')
    status = Column(String(20), comment='公開状態')
    update_date = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP"), comment='更新日')
    relationship = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='認知症のご本人から見たあなたの関係')
    relationship_etc = Column(Text, comment='認知症のご本人から見たあなたの関係のその他テキスト')
    gender = Column(INTEGER(11), nullable=False,
                    server_default=text("'0'"), comment='性別')
    birthday_era = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='認知症のご本人の生まれた年[年号]')
    birthday = Column(DateTime, nullable=False, server_default=text(
        "'0000-00-00 00:00:00'"), comment='認知症のご本人の生まれた年')
    address_code = Column(Text, nullable=False,
                          comment='認知症のご本人の住所の郵便番号(最初の3桁)')
    address_prefecture = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='認知症のご本人の住所の都道府県')
    dementia = Column(INTEGER(11), nullable=False,
                      server_default=text("'0'"), comment='認知症の診断の有無')
    cause_disease = Column(Text, nullable=False, comment='認知症の原因疾患(複数選択)')
    cause_disease_etc = Column(Text, comment='認知症の原因疾患のその他テキスト')
    nursing_level = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='要介護度')
    single_living = Column(INTEGER(11), nullable=False,
                           server_default=text("'0'"), comment='独居／非独居')
    job = Column(INTEGER(11), nullable=False,
                 server_default=text("'0'"), comment='認知症のご本人の職業')
    job_etc = Column(Text, comment='認知症のご本人の職業のその他テキスト')
    personality_sensitive = Column(
        INTEGER(11), nullable=False, server_default=text("'0'"), comment='元々の性格：神経症傾向')
    alcohol_drinking = Column(INTEGER(11), nullable=False, server_default=text(
        "'0'"), comment='アルコールについて：飲酒の有無、頻度')

    wp_gs_dementia_person = _relationship('WpGsDementiaPerson')


class WpGsMetaGroup(Base):
    __tablename__ = 'wp_gs_meta_groups'
    __table_args__ = (
        Index('sorted_wp_gs_meta_groups_idx',
              'wp_gs_meta_type_id', 'position', 'id'),
    )

    id = Column(BIGINT(20), primary_key=True)
    wp_gs_meta_type_id = Column(ForeignKey(
        'wp_gs_meta_type.id'), nullable=False, index=True, comment='入力を行う情報種別')
    wp_gs_meta_categories_id = Column(ForeignKey(
        'wp_gs_meta_categories.id'), nullable=False, index=True, comment='入力項目のカテゴリID')
    group_name = Column(String(128), nullable=False,
                        comment='グループを分けるdivタグのidに利用するグループ名称')
    group_type = Column(INTEGER(11), nullable=False,
                        comment='グループの表示種別(入力項目やセパレート等を指定)')
    group_label = Column(Text, comment='グループのラベル')
    group_attention = Column(Text, comment='group_labelの下に表示する注意書きの文章を設定する')
    group_help = Column(Text, comment='cssでヘルプ用の吹き出しを表示させるためのクラス名を設定')
    effect_class = Column(String(128), comment='グループにクラス名を付与してcssで制御するための設定値')
    another_visibility = Column(
        Text, nullable=False, comment='自分以外で表示するフラグ(0：非表示、1：表示、文字列：任意の表示)')
    required = Column(INTEGER(11), server_default=text("'0'"), comment='必須フラグ')
    position = Column(INTEGER(11), nullable=False, server_default=text(
        "'100'"), comment='グループの表示順を設定する(ソート用)')
    display_page = Column(INTEGER(11), nullable=False,
                          server_default=text("'0'"), comment='表示するページ番号')

    wp_gs_meta_categories = _relationship('WpGsMetaCategory')
    wp_gs_meta_type = _relationship('WpGsMetaType')


class WpGsCareinfoDpsMetaOption(Base):
    __tablename__ = 'wp_gs_careinfo_dps_meta_option'
    __table_args__ = (
        Index('wp_gs_careinfo_dps_meta_option_index', 'id', 'meta_field_name'),
    )

    id = Column(ForeignKey('wp_gs_careinfo_dps_meta.id', ondelete='CASCADE', onupdate='CASCADE'),
                primary_key=True, nullable=False, comment='認知症のご本人情報のスナップショットID')
    meta_field_name = Column(
        String(192), primary_key=True, nullable=False, comment='入力項目のフィールド名')
    value = Column(Text, comment='特殊な設定値')

    wp_gs_careinfo_dps_meta = _relationship('WpGsCareinfoDpsMeta')


class WpGsMetaField(Base):
    __tablename__ = 'wp_gs_meta_fields'
    __table_args__ = (
        Index('sorted_wp_gs_meta_fields_idx', 'wp_gs_meta_type_id',
              'wp_gs_meta_groups_id', 'position', 'id'),
    )

    id = Column(BIGINT(20), primary_key=True)
    wp_gs_meta_type_id = Column(ForeignKey(
        'wp_gs_meta_type.id'), nullable=False, index=True, comment='入力を行う情報種別')
    wp_gs_meta_groups_id = Column(ForeignKey(
        'wp_gs_meta_groups.id'), nullable=False, index=True, comment='入力項目のグループID')
    field_name = Column(String(128), nullable=False,
                        comment='inputタグのnameやidに利用するフィールド名称')
    field_label = Column(Text, comment='フィールドのラベル')
    input_type = Column(String(128), nullable=False,
                        comment='テキスト入力やチェックボックス等の入力項目の種類')
    input_format = Column(
        Text, comment='入力項目の表示形式の指定をする(通常は%inpu_value%で入力項目を表示できる)')
    input_example = Column(Text, comment='記入例')
    option_group = Column(BIGINT(20), comment='選択入力で使用する選択肢グループ')
    control_class = Column(
        String(128), comment='フィールドにクラス名を付与してjsやcssで制御するための設定値')
    effect_class = Column(String(128), comment='フィールドにクラス名を付与してcssで制御するための設定値')
    empty_visibility = Column(INTEGER(1), nullable=False, server_default=text(
        "'1'"), comment='未入力の項目について表示／非表示を設定する(0：非表示、1：表示)')
    empty_display = Column(Text, comment='未入力時の表示内容')
    another_label = Column(Text, nullable=False, comment='自分以外で表示するラベル')
    another_display = Column(Text, nullable=False,
                             comment='自分以外で表示する内容(0：非表示、1：表示、ファイル名：任意の形式)')
    reference_field = Column(Text, comment='参照元フィールド')
    required = Column(Text, nullable=False,
                      comment='必須フラグ(0:省略可、1:必須、依存フィールド名:依存先のフィールドにより必須)')
    position = Column(INTEGER(11), nullable=False, server_default=text(
        "'100'"), comment='フィールドの表示順を設定する(ソート用)')

    wp_gs_meta_groups = _relationship('WpGsMetaGroup')
    wp_gs_meta_type = _relationship('WpGsMetaType')
