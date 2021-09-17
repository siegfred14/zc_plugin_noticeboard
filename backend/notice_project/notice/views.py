from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from rest_framework import views, status, views
from .storage import db
from .serializers import NoticeboardRoom, CreateNoticeSerializer
from rest_framework.generics import ListAPIView
import uuid


@api_view(['GET'])
def sidebar(request):

    org_id = request.GET.get('org')
    user_id = request.GET.get('user')

    if org_id and user_id:

        res = requests.get(
            f"https://api.zuri.chat/organizations/{org_id}/members/{user_id}").json()

        if res['status'] == 200:

            res = requests.get("noticeboard_room", org_id).json()
            if res['status'] == 200 and res is not None:
                public_rooms = res['data']
            else:
                public_rooms = []

            sidebar = {
                "name": "Noticeboard Plugin",
                "description": "Displays Information On A Noticeboard",
                        "plugin_id": "613fc3ea6173056af01b4b3e",
                        "organisation_id": f"{org_id}",
                        "user_id": f"{user_id}",
                        "group_name": "Noticeboard",
                        "show_group": False,
                        "joined_rooms": [],
                        "public_rooms": public_rooms
            }
            return Response({"status": True, "data": sidebar}, status=status.HTTP_200_OK)
        return Response({"status": False, "message": res["message"]}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": False, "message": "Check your query parameter"})


@api_view(['POST'])
def create_room(request, org_id):
    # org_id = "613a1a3b59842c7444fb0220"
    serializer = NoticeboardRoom(data=request.data)
    if serializer.is_valid():
        db.save("noticeboard_room", org_id, serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_room(request, org_id):
    # org_id = "613a1a3b59842c7444fb0220"
    data = db.read("noticeboard_room", org_id)
    return Response(data)


@api_view(['GET'])
def install(request):
    org_id = "613a1a3b59842c7444fb0220"

    data = {
        "room_id": uuid.uuid4(),
        "title": "noticeboard",
        "unread": "0",
        "members": "0",
        "icon": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRr-kPo-vAmp_GrCZbnmqT6PMU5Wi5BLwgvPQ&usqp=CAU",
        "action": "open"
    }

    requests.post(
        f"https://noticeboard.zuri.chat/api/v1/{org_id}/create-room", data=data)
    # requests.post("http://localhost:8000/api/v1/create-notice-room", data=data)

    install = {
        "name": "Noticeboard Plugin",
        "description": "Creates Notice",
        "plugin_id": "613fc3ea6173056af01b4b3e",
    }
    return Response(install)


class CreateNewNotices(views.APIView):

    '''
    Create new notices
    '''

    def post(self, request, org_id):
        serializer = CreateNoticeSerializer(data=request.data)

        if serializer.is_valid():
            db.save(
                "noticeboard",
                # "613a1a3b59842c7444fb0220",
                org_id,
                notice_data=serializer.data
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateNoticeAPIView(views.APIView):

    def put(self, request, org_id):
        serializer = CreateNoticeSerializer(data=request.data)
        if serializer.is_valid():
            db.update(
                "noticeboard",
                # "613a1a3b59842c7444fb0220",
                org_id,
                serializer.data,
                object_id="613e4cf015fb2424261b6633")
            return Response(
                {
                    "success": True,
                    "data": serializer.data,
                    "message": "Notice has been successfully updated"
                },
                status=status.HTTP_201_CREATED)
        return Response(
            {
                "success": False,
                "message": "Notice not updated, Please Try Again"
            },
            status=status.HTTP_400_BAD_REQUEST)


class search(ListAPIView):
    def get(self, request):

        org_id = "613a1a3b59842c7444fb0220"

        notice = db.read("noticeboard", org_id)
        if notice['status'] == 200:
            all_notice = notice['data']
            query = request.GET.get("q")

            if query:
                all_notice = list(
                    filter(lambda x: x['title'] == query, all_notice))
            return Response(
                {
                    "status": True,
                    "data": all_notice,
                    "message": "Successfully retrieved"
                },
                status=status.HTTP_200_OK)
        return Response(
            {
                "success": False,
                "message": "Failed"
            },
            status=status.HTTP_400_BAD_REQUEST)


class ViewNoticeAPI(views.APIView):

    def get(self, request, org_id):
        notice = db.read("noticeboard", org_id)
        if notice['status'] == 200:
            return Response(notice, status=status.HTTP_200_OK)
        return Response({"status": False, "message": "retrieved unsuccessfully"}, status=status.HTTP_400_BAD_REQUEST)


# class NoticeDetail(views.APIView):
    # find notice by pk (id)

    # def get(self, pk):
    #     notice = db.read("noticeboard", "613a1a3b59842c7444fb0220")
    #     try:
    #         notice_detail = notice.objects.get(pk=pk)
    #     except notice.DoesNotExist:
    #         return JsonResponse({'message': 'Notice does not exist'}, status=status.HTTP_404_NOT_FOUND)
