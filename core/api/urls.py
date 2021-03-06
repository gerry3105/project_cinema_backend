from django.urls import path

from .views import (NowPlayingMovies, OpeningThisWeekMovies, CategoryView,
                    AllTheaters, MovieScreenings, PerformBookingView, GetFreeSeatsView,)

urlpatterns = [
    path('book_a_ticket/<int:screening_id>/<str:seat>/', PerformBookingView.as_view(), name='book_a_ticket'),
    path('get_free_seats/<int:pk>', GetFreeSeatsView.as_view(), name='get_free_seats'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('movie_screenings/<int:pk>', MovieScreenings.as_view(), name='movie_screenings'),
    path('now_playing_movies/', NowPlayingMovies.as_view(), name='now_playing_movies'),
    path('opening_this_week_movies/', OpeningThisWeekMovies.as_view(), name='opening_this_week_movies'),
    path('theaters/', AllTheaters.as_view(), name='theaters'),
]