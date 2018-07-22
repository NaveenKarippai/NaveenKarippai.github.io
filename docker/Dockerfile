FROM alpine
RUN apk add python			     # add python2.x
COPY requirements.txt /tmp
WORKDIR /tmp
RUN apk update && apk add py-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apk update && apk add git tmux
RUN apk --update add less		     # add GNU less
RUN apk add git-perl 			     # fix interactive staging
RUN git config --global core.pager 'less -R' # fix colors in git diff
