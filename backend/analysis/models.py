from django.db import models


class Analysis(models.Model):
    # 결과 값을 SAFE/DANGER 두 개로 한 곳에 정의
    class Result(models.TextChoices):
        SAFE = "SAFE", "위험 미감지"
        DANGER = "DANGER", "위험 감지"

    video = models.FileField(upload_to='videos/')
    # NOTE: null = 아직 분석 전 (영상 먼저 저장, AI 결과는 나중에 UPDATE)
    result = models.CharField(max_length=10, choices=Result.choices, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)