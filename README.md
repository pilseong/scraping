# Scraping 패턴 정리
D&A 용으로 분석할 자료 추출용 및 기타 실시간 자료 추출 자동화를 위한 스크립트를 모아 두려는 목적으로 생성한 Repositry. 아래는 각 사용하는 라이브러리 마다 추가하여 정리할 생각으로 생성

## 1. Beautiful Soup
### 장점
* 단순한 구조로 쉽게 스크립트 작성가능
* 속도도 일반 request처리와 비슷
### 단점
* 자바스크립트로 만들어진 동적 페이지는 접근하여 추출하기 힘듦
### Dependency
* bs4, lxml, requests를 의존하고 있다. pip으로 설치하여 사용한다.
### 소스
* 참조용 스크립트로 TISTORY 개인 블로그의 글을 모두 가져오는 스크립트(pageWithPagination_tistory.py)를 추가하였다.

## 2. Selenium 

## 3. Scrapy

## 4. Puppeteer
...