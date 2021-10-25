# 2기 - 레이서 포트폴리오 서비스 - 정태윤

## 1. 프로젝트 소개
회원가입 후, 사용자의 포트폴리오를 업로드하고, 관리할 수 있는 풀스택 CRUD 웹 서비스입니다.

## 2. 구현 기능
1. 인증 및 권한
2. 포트폴리오 CRUD
3. 사용자 검색

## 3. 사용 기술
- Flask
- MySQL
- Azure Cloue Storage
- Javascript
- React.js Functional Components + Hook

## 4. [API 문서](https://documenter.getpostman.com/view/7766107/Tzz8td4m)

## 5. 프로젝트 구조
```
.
├── backend
│   ├── racer_portfolio
│   │   ├── apis
│   │   ├── models
│   │   ├── services
│   │   └── utils
│   └── scripts
└── frontend
    ├── public
    └── src
        ├── apis
        ├── components
        │   └── portfolio
        ├── pages
        ├── styles
        └── utils
```

## 6. 데이터베이스 ERD
![포트폴리오_erd](https://kdt-gitlab.elice.io/002-part2-project-portfolio/team2/jeongtaeyoon/-/wikis/uploads/7f5aae23a15210dc98b8aa765e1c5ad9/%ED%8F%AC%ED%8A%B8%ED%8F%B4%EB%A6%AC%EC%98%A4_erd.png)