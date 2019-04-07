from . import main
from flask import render_template, request, url_for, redirect, abort, flash
from app.models import Image, Article, db, Comment


# 首页
@main.route('/')
def index():
    return 'Hello Flask !'


# 图片列表页面
@main.route('/image/index', methods=['GET'])
def image_index():
    page = int(request.args.get('page') or 1)
    per_page = int(request.args.get('perpage') or 15)

    paginate = Image.query.paginate(page, per_page, error_out=False)
    image_list = paginate.items
    return render_template('image.html', images=image_list, paginate=paginate)


# 文章创建,编辑保存
@main.route('/article/create', methods=['GET', 'POST'])
def article_create():
    if request.method == "GET":
        return render_template('article/create.html')
    elif request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        article_id = request.form.get('article_id')

        newArticle = Article(title=str(title), content=str(content))

        try:
            if article_id:
                article = Article.query.filter_by(id=article_id).first()
                article.title = title
                article.content = content

            else:
                db.session.add(newArticle)
            db.session.commit()

        except:
            db.session.rollback()

        finally:
            return redirect(url_for('main.article_index'))


# 文章保存
@main.route('/article/index', methods=['GET'])
def article_index():
    page = int(request.args.get('page') or 1)
    perpage = int(request.args.get('perpage') or 4)

    paginate = Article.query.paginate(page, perpage, error_out=False)
    articles = paginate.items
    return render_template('article/index.html', articles=articles, paginate=paginate)


# 编辑
@main.route('/article/edit', methods=['POST'])
def article_edit():
    article_id = request.form.get('article_id')

    article = Article.query.filter_by(id=article_id).first()
    return render_template('/article/edit.html', article=article)


# 浏览
@main.route('/article/view', methods=['GET'])
def article_view():
    article_id = request.args.get('article_id')

    if article_id:
        article = Article.query.filter_by(id=article_id).first()
        return render_template('/article/view.html', article=article)
    else:
        abort(404)


# 文章评论
@main.route('/article/comment', methods=['POST'])
def article_comment():
    article_id = request.form.get('article_id')
    detail = request.form.get('detail')
    user_id = 0

    newComment = Comment(
        article_id=article_id,
        detail=str(detail),
        user_id=user_id
    )

    try:
        db.session.add(newComment)
        db.session.commit()

    except IntegrityError as e:
        db.session.rollback()

    finally:
        return redirect(url_for('main.article_view', article_id=article_id))
