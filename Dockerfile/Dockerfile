
FROM ubuntu:24.04

LABEL maintainer="joaodanilo1992@gmail.com"
LABEL version="0.1"
LABEL description="Environmnet for appium tests"

WORKDIR "/workdir"


ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y  curl unzip \
                        openjdk-21-jdk \
                        ffmpeg \
                        libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio

# ------ Install node 22 -------------
ENV NODE_VERSION=22
ENV NVM_DIR=/root/.nvm
ENV PATH="$NVM_DIR/versions/node/v${NODE_VERSION}/bin/:${PATH}"

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}


# ------ Install appium -------------
RUN . "$NVM_DIR/nvm.sh" && npm install -g appium
RUN . "$NVM_DIR/nvm.sh" && appium driver install uiautomator2

# ------ Android stuff download
ENV ANDROID_HOME=/workdir/android/
RUN mkdir /workdir/android

RUN curl "https://dl.google.com/android/repository/platform-tools-latest-linux.zip" -o /workdir/android/platform-tools-latest-linux.zip
RUN unzip /workdir/android/platform-tools-latest-linux.zip -d /workdir/android/ && rm /workdir/android/platform-tools-latest-linux.zip
ENV PATH="/workdir/android/platform-tools:${PATH}"

RUN curl -L "https://redirector.gvt1.com/edgedl/android/repository/emulator-linux_x64-13823996.zip" -o /workdir/android/emulator-linux_x64-13823996.zip
RUN unzip /workdir/android/emulator-linux_x64-13823996.zip -d /workdir/android/ && rm /workdir/android/emulator-linux_x64-13823996.zip

ENV PATH="/workdir/android/bundle-tools/:${PATH}"
RUN mkdir /workdir/android/bundle-tools
RUN curl "https://github.com/google/bundletool/releases/download/1.18.1/bundletool-all-1.18.1.jar" -o /workdir/android/bundle-tools/bundletool.jar
RUN chmod +x /workdir/android/bundle-tools/bundletool.jar

# ------ Java stuff configuration

ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64/

EXPOSE 4723

CMD ["/bin/bash", "-c", ". $NVM_DIR/nvm.sh && appium --relaxed-security --base-path /wd/hub"]




