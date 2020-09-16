import logging

logger = logging.getLogger("main")

class CommonMiddleware(object):
    """
    リクエストとレスポンスの共通処理
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        self.process_response(request, response)

        return response

    def process_request(self, request):
        """
        前処理
        :param request:
        :return:
        """
        logger.info("リクエストの処理")

    def process_response(self, request, response):
        """
        後処理
        :param request:
        :param response:
        :return:
        """
        logger.info("レスポンスの処理")