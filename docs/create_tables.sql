DROP TABLE IF EXISTS category;

CREATE TABLE category(
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT 'id',
    c_name VARCHAR(20) NOT NULL UNIQUE COMMENT '大类名称'
)ENGINE=InnoDB DEFAULT CHARSET=utf8 comment='大类表';


DROP TABLE IF EXISTS college;

CREATE TABLE college(
    id INT PRIMARY KEY AUTO_INCREMENT,
    c_name VARCHAR(30) NOT NULL UNIQUE COMMENT '学院名称',
    category_id INT NOT NULL COMMENT '大类id，外键',
    CONSTRAINT fk_college_category FOREIGN KEY (category_id) REFERENCES category(id) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8 comment='学院表';


DROP TABLE IF EXISTS interest;

CREATE TABLE interest(
    id INT PRIMARY KEY AUTO_INCREMENT,
    i_name VARCHAR(20) NOT NULL UNIQUE COMMENT '标签名称'
)ENGINE=InnoDB DEFAULT CHARSET=utf8 comment='兴趣标签表';


DROP TABLE IF EXISTS major;

CREATE TABLE major(
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '专业id',
    m_name VARCHAR(20) NOT NULL UNIQUE COMMENT '专业名称',
    college_id INT NOT NULL COMMENT '所属学院id，外键',
    category_id INT NOT NULL COMMENT '所属大类id，外键',
    intro VARCHAR(1000) NOT NULL DEFAULT '' COMMENT '专业介绍',
    course VARCHAR(800) COMMENT '专业课程',
    salary VARCHAR(200) COMMENT '薪资水平',
    rank_precent VARCHAR(50) COMMENT '专业类内排位百分比',
    CONSTRAINT fk_major_college FOREIGN KEY (college_id) REFERENCES college(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_major_category FOREIGN KEY (category_id) REFERENCES category(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8 comment='专业表';


DROP TABLE IF EXISTS interest2major;

CREATE TABLE interest2major(
    id INT PRIMARY KEY AUTO_INCREMENT,
    interest_id INT NOT NULL COMMENT '兴趣标签ID',
    major_id INT NOT NULL COMMENT '专业ID',
    FOREIGN KEY (interest_id) REFERENCES interest(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (major_id) REFERENCES major(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8 comment='兴趣和专业对应关系表';


DROP TABLE IF EXISTS cty_mj_rk;

CREATE TABLE cty_mj_rk(
    id INT PRIMARY KEY AUTO_INCREMENT,
    cty_id INT NOT NULL COMMENT '大类名称id，外键',
    mj_id INT NOT NULL COMMENT '专业名称id，外键',
    first_precent FLOAT COMMENT '第一年百分比',
    second_precent FLOAT COMMENT '第二年百分比',
    third_precent FLOAT COMMENT '第三年百分比',
    FOREIGN KEY (cty_id) REFERENCES category(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (mj_id) REFERENCES major(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8 comment='大类-专业-近三年排名，为了专业一览的分流排位';

DROP TABLE IF EXISTS board;

CREATE TABLE board(
    id INT PRIMARY KEY AUTO_INCREMENT,
    b_name VARCHAR(80) UNIQUE NOT NULL COMMENT '板块名称',
    publish_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    intro VARCHAR(200) COMMENT '板块介绍'

)ENGINE=InnoDB DEFAULT CHARSET=utf8 comment='发布页面的板块';

DROP TABLE IF EXISTS article;

CREATE TABLE article(
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(80) UNIQUE NOT NULL COMMENT '板块名称',
    publish_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '发布时间',
    content VARCHAR(8888) COMMENT '文章内容',
    author VARCHAR(30) COMMENT '作者',
    board_id INT NULL COMMENT '所属板块',
    img_link VARCHAR(8888) COMMENT '图片链接，逗号分隔',
    file_link VARCHAR(8888) COMMENT '所需下载文档链接，逗号分隔',
    CONSTRAINT fk_article_board FOREIGN KEY (board_id) REFERENCES board(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 comment='文章的表';







