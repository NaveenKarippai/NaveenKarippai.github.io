# add base image
FROM alpine
# add python2.x
RUN apk add python
COPY requirements.txt /tmp
WORKDIR /tmp
RUN apk update && apk add py-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# install required packages
RUN apk update && apk add git tmux make openssh vim
# add GNU less
RUN apk --update add less
# fix interactive staging
RUN apk add git-perl
# fix colors in git diff
RUN git config --global core.pager "less -R"
RUN git config --global user.name "NaveenKarippai"
RUN git config --global user.email naveenranjankarippai@gmail.com
# expose port
EXPOSE 8000/tcp
# add user named tux
RUN adduser -D -g 'penguin' tux
USER tux
WORKDIR /home/tux
