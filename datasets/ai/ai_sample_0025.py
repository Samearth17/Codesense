apiVersion: v1
kind: Pod
metadata:
  name: tweet-publisher
spec:
  containers:
    - name: tweet-publisher
      image: <INSERT_PUBLIC_PULLABLE_IMAGE_PATH_HERE>
      command:
        - sh
        - -c
        - 'crontab -lcrontab && while true; do python publish-tweet.py && crontab -l | { cat; echo "*/5 * * * * python publish-tweet.py"; } | crontab -; sleep 31622400; done'
      volumeMounts:
        - mountPath: /crontab/crontab
          subPath: crontab
          name: cronmount
  volumes:
    - name: cronmount
      configMap:
        name: tweet-cron
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: tweet-cron
data:
  crontab: "* * * * * python publish-tweet.py"