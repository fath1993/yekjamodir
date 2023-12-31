from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect

from accounts.models import Profile
from documents.models import Folder, Document
from gallery.models import FileGallery


def folder_new(request):
    context = {'page_title': 'سند جدید - ',
               'navigation_icon_menu_id': 'service',
               'navigation_menu_body_id': 'navigationService',
               'navigation_menu_body_sub_item_id': 'folder-new',
               }
    if request.user.is_authenticated:
        if request.method == 'GET':
            folders = Folder.objects.filter(created_by=request.user)
            context['folders'] = folders
            return render(request, 'documents/folder-new.html', context)
        else:
            try:
                folder_parent = request.POST['folder-parent']
                if str(folder_parent).replace(' ', '') == '-':
                    folder_parent = None
            except:
                folder_parent = None

            try:
                folder_title = request.POST['folder-title']
                if folder_title == ' - ':
                    folder_title = None
            except:
                folder_title = None

            if folder_title is not None:
                try:
                    folder_parent = Folder.objects.get(id=int(folder_parent))
                except:
                    folder_parent = None

            new_folder = Folder(
                parent=folder_parent,
                title=folder_title,
                created_by=request.user,
            )
            new_folder.save()
            return redirect('documents:folder-list')
    else:
        return redirect('accounts:login')


def folder_list(request):
    context = {'page_title': 'سند جدید - ',
               'navigation_icon_menu_id': 'service',
               'navigation_menu_body_id': 'navigationService',
               'navigation_menu_body_sub_item_id': 'folder-list',
               }
    if request.user.is_authenticated:
        if request.method == 'GET':
            folders = Folder.objects.filter(created_by=request.user)
            context['folders'] = folders
            return render(request, 'documents/folder-list.html', context)
        else:
            try:
                folder_parent = request.POST['folder-parent']
                if str(folder_parent).replace(' ', '') == '-':
                    folder_parent = None
            except:
                folder_parent = None

            try:
                folder_title = request.POST['folder-title']
                if folder_title == ' - ':
                    folder_title = None
            except:
                folder_title = None

            if folder_title is not None:
                try:
                    folder_parent = Folder.objects.get(id=int(folder_parent))
                except:
                    folder_parent = None

            new_folder = Folder(
                parent=folder_parent,
                title=folder_title,
                created_by=request.user,
            )
            new_folder.save()
            return redirect('documents:folder-list')
    else:
        return redirect('accounts:login')


def folder_edit(request, folder_id):
    context = {'page_title': 'ویرایش پوشه - ',
               'navigation_icon_menu_id': 'service',
               'navigation_menu_body_id': 'navigationService',
               'navigation_menu_body_sub_item_id': 'folder-list',
               }
    if request.user.is_authenticated:
        if request.method == 'GET':
            folders = Folder.objects.filter(created_by=request.user)
            context['folders'] = folders
            folder = Folder.objects.get(id=folder_id, created_by=request.user)
            context['folder'] = folder
            return render(request, 'documents/folder-edit.html', context)
        else:
            try:
                folder_parent = request.POST['folder-parent']
                if str(folder_parent).replace(' ', '') == '-':
                    folder_parent = None
            except:
                folder_parent = None

            try:
                folder_title = request.POST['folder-title']
                if folder_title == ' - ':
                    folder_title = None
            except:
                folder_title = None

            if folder_title is not None:
                try:
                    folder_parent = Folder.objects.get(id=int(folder_parent))
                except:
                    folder_parent = None

            folder = Folder.objects.get(id=folder_id, created_by=request.user)
            folder.parent = folder_parent
            folder.title = folder_title
            folder.save()
            return redirect('documents:folder-list')
    else:
        return redirect('accounts:login')


def folder_delete(request, folder_id):
    context = {'page_title': 'حذف پوشه - '}
    if request.user.is_authenticated:
        if request.method == 'GET':
            folder = Folder.objects.get(id=folder_id, created_by=request.user)
            folder.delete()
            return redirect('documents:folder-list')
    else:
        return redirect('accounts:login')


def document_new(request):
    context = {'page_title': 'سند جدید - ',
               'navigation_icon_menu_id': 'service',
               'navigation_menu_body_id': 'navigationService',
               'navigation_menu_body_sub_item_id': 'document-new',
               }
    if request.user.is_authenticated:
        if request.method == 'GET':
            folders = Folder.objects.filter(created_by=request.user)
            context['folders'] = folders
            profiles = Profile.objects.all()
            employees = profiles.filter(is_employee=True)
            others = profiles.filter(is_employee=False)
            context['employees'] = employees
            context['others'] = others
            return render(request, 'documents/document-new.html', context)
        else:
            try:
                folder_id = request.POST['folder']
                if folder_id == ' - ':
                    folder_id = None
            except:
                folder_id = None

            try:
                document_title = request.POST['document-title']
                if document_title == ' - ':
                    document_title = None
            except:
                document_title = None
            try:
                document_description = request.POST['document-description']
                if document_description == ' - ':
                    document_description = None
            except:
                document_description = None
            try:
                access_user = request.POST.getlist('access-user')
                if access_user == ' - ':
                    access_user = None
            except Exception as e:
                print(str(e))
                access_user = None
            print(folder_id)
            print(document_title)
            print(document_description)
            print(access_user)
            folder = Folder.objects.get(id=folder_id, created_by=request.user)
            new_document = Document(
                folder=folder,
                title=document_title,
                description=document_description,
                created_by=request.user,
            )
            new_document.save()
            return redirect('documents:document-edit', document_id=new_document.id)
    else:
        return redirect('accounts:login')


def document_list(request):
    context = {'page_title': 'لیست اسناد - ',
               'navigation_icon_menu_id': 'service',
               'navigation_menu_body_id': 'navigationService',
               'navigation_menu_body_sub_item_id': 'document-list',
               }
    if request.user.is_authenticated:
        if request.method == 'GET':
            self_documents = Document.objects.filter(created_by=request.user, document_parent=None)
            context['self_documents'] = self_documents
            shared_documents = Document.objects.filter(allowed_to__id__exact=request.user.id)
            shared_documents_list = []
            for shared_document in shared_documents:
                if shared_document.created_by != request.user:
                    shared_documents_list.append(shared_document)
            context['shared_documents'] = set(shared_documents_list)
            return render(request, 'documents/document-list.html', context)
        else:
            try:
                folder_parent = request.POST['folder-parent']
                if folder_parent == ' - ':
                    folder_parent = None
            except:
                folder_parent = None

            try:
                folder_title = request.POST['folder-title']
                if folder_title == ' - ':
                    folder_title = None
            except:
                folder_title = None
            print(folder_parent)
            print(folder_title)
    else:
        return redirect('accounts:login')


def document_edit_history_list(request, document_id):
    context = {'navigation_icon_menu_id': 'service',
               'navigation_menu_body_id': 'navigationService',
               'navigation_menu_body_sub_item_id': 'document-list',
               }
    if request.user.is_authenticated:
        if request.method == 'GET':
            document = Document.objects.get(id=document_id)
            context['page_title'] = 'سوابق ویرایش سند: ' + str(document.title)
            documents = Document.objects.filter(document_parent=document).order_by('-created_at')
            context['documents'] = documents
            return render(request, 'documents/document-edit-history-list.html', context)
        else:
            try:
                folder_parent = request.POST['folder-parent']
                if folder_parent == ' - ':
                    folder_parent = None
            except:
                folder_parent = None

            try:
                folder_title = request.POST['folder-title']
                if folder_title == ' - ':
                    folder_title = None
            except:
                folder_title = None
            print(folder_parent)
            print(folder_title)
    else:
        return redirect('accounts:login')


def document_delete(request, document_id):
    context = {'page_title': 'حذف سند - '}
    if request.user.is_authenticated:
        if request.method == 'GET':
            document = Document.objects.get(id=document_id, created_by=request.user)
            document.delete()
            return redirect('documents:folder-list')
    else:
        return redirect('accounts:login')


def document_edit(request, document_id):
    context = {'page_title': 'ویرایش سند - ',
               'navigation_icon_menu_id': 'service',
               'navigation_menu_body_id': 'navigationService',
               'navigation_menu_body_sub_item_id': 'document-list',
               }
    if request.user.is_authenticated:
        if request.method == 'GET':
            try:
                document = Document.objects.get(id=document_id, created_by=request.user)
            except:
                try:
                    document = Document.objects.get(id=document_id, allowed_to__id__exact=request.user.id)
                except:
                    return redirect('documents:document-list')

            context['document'] = document
            context['access_users'] = document.allowed_to.all()
            profiles = Profile.objects.all()
            employees = profiles.filter(is_employee=True)
            others = profiles.filter(is_employee=False)
            context['employees'] = employees
            context['others'] = others
            return render(request, 'documents/document-edit.html', context)
        else:
            try:
                content = request.POST['content']
                if content == '':
                    content = None
            except:
                content = None
            try:
                files = request.FILES.getlist('files')
                if files == '':
                    files = None
            except Exception as e:
                print(str(e))
                files = None
            try:
                access_user = request.POST.getlist('access-user')
                if access_user == '':
                    access_user = None
            except:
                access_user = None
            try:
                document = Document.objects.get(id=document_id, created_by=request.user)
            except:
                try:
                    document = Document.objects.get(id=document_id, allowed_to__id__exact=request.user.id)
                except:
                    return redirect('documents:document-list')

            if document.created_by == request.user:  # current document will be edited and the new one is generated
                new_document = Document(
                    document_parent=document,
                    folder=document.folder,
                    title=document.title,
                    description=document.description,
                    content=content,
                    created_by=request.user,
                )
                new_document.save()
                document.content = content
                for file in files:
                    try:
                        file = FileGallery.objects.get(file=file, created_by=request.user)
                    except:
                        file = FileGallery(
                            alt=file.name,
                            file=file,
                            created_by=request.user
                        )
                        file.save()
                    document.files.add(file)
                    new_document.files.add(file)
                    document.save()
                    new_document.save()
                for user_id in access_user:
                    user = User.objects.get(id=user_id)
                    document.allowed_to.add(user)
                    new_document.allowed_to.add(user)
                    document.save()
                    new_document.save()
                return redirect('documents:document-edit', document_id=document.id)
            else:  # only new document is generated
                new_document = Document(
                    document_parent=document,
                    folder=document.folder,
                    title=document.title,
                    description=document.description,
                    content=content,
                    created_by=request.user,
                )
                new_document.save()
                for file in files:
                    try:
                        file = FileGallery.objects.get(file=file, created_by=request.user)
                    except:
                        file = FileGallery(
                            alt=file.name,
                            file=file,
                            created_by=request.user
                        )
                        file.save()
                    new_document.files.add(file)
                    new_document.save()
                for user_id in access_user:
                    user = User.objects.get(id=user_id)
                    new_document.allowed_to.add(user)
                    new_document.save()
                return redirect('documents:document-edit', document_id=new_document.id)
    else:
        return redirect('accounts:login')


def ajax_file_delete(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            file_id = request.POST['file_id']
            try:
                file = FileGallery.objects.get(id=int(file_id), created_by=request.user)
                file.delete()
                return JsonResponse({"message": "ok"})
            except:
                return JsonResponse({"message": "failed"})
