import os,json
from . import main
from flask import render_template, request, url_for, redirect, abort, flash, jsonify, Response
from app.models import Image, Article, db, Comment, Category, City, Poi, Monitor


# 首页
@main.route('/')
def index():
    return render_template('index.html')


# 图片列表页面
@main.route('/image/index', methods=['GET'])
def image_index():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('perpage', 10, type=int)

    paginate = Image.query.paginate(page, per_page, error_out=False)
    image_list = paginate.items
    return render_template('/image/list.html', images=image_list, paginate=paginate)


# 图片列表页面
@main.route('/image/view', methods=['GET'])
def image_view():
    image_id = request.args.get('id', 1, type=int)
    image = Image.query.filter_by(id=image_id).first()
    return render_template('/image/view.html', image=image)


# 文章创建,编辑保存
@main.route('/article/create', methods=['GET', 'POST'])
def article_create():
    if request.method == "GET":
        return render_template('article/create.html')
    elif request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        article_id = request.form.get('article_id')

        new_article = Article(title=str(title), content=str(content))

        try:
            if article_id:
                article = Article.query.filter_by(id=article_id).first()
                article.title = title
                article.content = content

            else:
                db.session.add(new_article)
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


# poi 分类数据列表
@main.route('/poi/category', methods=['GET'])
def poi_category():
    cat_id = int(request.args.get('cat_id') or 0)
    if not cat_id:
        cats = Category.query.all()
        for cat in cats:
            cat.img_url = 'images/' + cat.pinyin + '.png'
    return render_template('/poi/category.html', cats=cats)


# poi 分类下的城市数据
@main.route('/poi/<category_name>', methods=['GET'])
def poi_city(category_name):
    city_name = request.args.get('city_name') or ''
    cities = City.query.all()

    if city_name:
        page = int(request.args.get('page') or 1)
        perpage = int(request.args.get('perpage') or 10)

        nq = Poi.query.filter_by(city=city_name)
        paginate = nq.paginate(page, perpage, error_out=False)
        points = paginate.items
        for point in points:
            point.addr = point.province +' ' + point.region + ' '+ point.location
            point.name_display = point.name[0:10]

        return render_template(
            '/poi/list.html',
            points=points,
            category_name=category_name,
            city_name=city_name,
            paginate=paginate,
            cur_page=page
        )
    else:
        return render_template(
            '/poi/city.html',
            cities=cities,
            category_name=category_name,
            city_name=city_name
        )


# cpu页面
@main.route('/tools/cpu', methods=['GET'])
def tools_cpu():
    return render_template('/tools/cpu.html')

# cpu 占用率数据
@main.route('/tools/cpu_monitor', methods=['GET'])
def tools_cpu_monitor():
    # 从DB读取曲线绘制的数据信息;
    data = Monitor.query.order_by('id').limit(50).all()
    return jsonify(data)